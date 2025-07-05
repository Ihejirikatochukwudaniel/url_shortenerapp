from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, abort
from models import db, URL, ClickLog
from flask_sqlalchemy import SQLAlchemy
from config import Config
import validators
from datetime import datetime
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize database
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    return app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form.get('url', '').strip()
    
    if not original_url:
        flash('Please enter a URL', 'error')
        return redirect(url_for('index'))
    
    # Add http:// if no protocol specified
    if not original_url.startswith(('http://', 'https://')):
        original_url = 'http://' + original_url
    
    # Validate URL
    if not validators.url(original_url):
        flash('Please enter a valid URL', 'error')
        return redirect(url_for('index'))
    
    # Check if URL already exists
    existing_url = URL.query.filter_by(original_url=original_url).first()
    if existing_url:
        short_url = f"{app.config['BASE_URL']}/{existing_url.short_code}"
        flash(f'URL already shortened: {short_url}', 'info')
        return render_template('index.html', short_url=short_url, short_code=existing_url.short_code)
    
    # Create new short URL
    short_code = URL.generate_short_code(app.config['SHORT_URL_LENGTH'])
    new_url = URL(
        original_url=original_url,
        short_code=short_code,
        creator_ip=request.remote_addr
    )
    
    try:
        db.session.add(new_url)
        db.session.commit()
        
        short_url = f"{app.config['BASE_URL']}/{short_code}"
        flash(f'URL shortened successfully!', 'success')
        return render_template('index.html', short_url=short_url, short_code=short_code)
    
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while shortening the URL', 'error')
        return redirect(url_for('index'))

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url = URL.query.filter_by(short_code=short_code).first()
    
    if not url:
        abort(404)
    
    # Log the click
    click_log = ClickLog(
        url_id=url.id,
        ip_address=request.remote_addr,
        user_agent=request.headers.get('User-Agent', ''),
        referer=request.headers.get('Referer', '')
    )
    
    # Update click count
    url.clicks += 1
    
    try:
        db.session.add(click_log)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error logging click: {e}")
    
    return redirect(url.original_url)

@app.route('/stats/<short_code>')
def url_stats(short_code):
    url = URL.query.filter_by(short_code=short_code).first()
    
    if not url:
        abort(404)
    
    # Get click statistics
    recent_clicks = ClickLog.query.filter_by(url_id=url.id).order_by(ClickLog.clicked_at.desc()).limit(10).all()
    
    # Get daily click stats for the last 7 days
    daily_stats = db.session.query(
        db.func.date(ClickLog.clicked_at).label('date'),
        db.func.count(ClickLog.id).label('clicks')
    ).filter(
        ClickLog.url_id == url.id,
        ClickLog.clicked_at >= datetime.utcnow().date() - db.text('INTERVAL 7 DAY')
    ).group_by(db.func.date(ClickLog.clicked_at)).all()
    
    return render_template('stats.html', url=url, recent_clicks=recent_clicks, daily_stats=daily_stats)

@app.route('/api/stats/<short_code>')
def api_stats(short_code):
    url = URL.query.filter_by(short_code=short_code).first()
    
    if not url:
        return jsonify({'error': 'URL not found'}), 404
    
    return jsonify({
        'short_code': url.short_code,
        'original_url': url.original_url,
        'total_clicks': url.clicks,
        'created_at': url.created_at.isoformat(),
        'short_url': f"{app.config['BASE_URL']}/{url.short_code}"
    })

@app.route('/all-urls')
def all_urls():
    urls = URL.query.order_by(URL.created_at.desc()).limit(50).all()
    return render_template('all_urls.html', urls=urls)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/favicon.ico')
def favicon():
    return '', 204  # No Content




if __name__ == '__main__':
    app.run(debug=True)