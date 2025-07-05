from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random

db = SQLAlchemy()

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text, nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    clicks = db.Column(db.Integer, default=0)
    creator_ip = db.Column(db.String(45))
    
    # Relationship with click tracking
    click_logs = db.relationship('ClickLog', backref='url', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<URL {self.short_code}>'
    
    @staticmethod
    def generate_short_code(length=6):
        """Generate a random short code for the URL"""
        characters = string.ascii_letters + string.digits
        while True:
            short_code = ''.join(random.choice(characters) for _ in range(length))
            if not URL.query.filter_by(short_code=short_code).first():
                return short_code

class ClickLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey('url.id'), nullable=False)
    clicked_at = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(45))
    user_agent = db.Column(db.Text)
    referer = db.Column(db.Text)
    
    def __repr__(self):
        return f'<ClickLog {self.id}>'