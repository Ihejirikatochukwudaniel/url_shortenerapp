# 🔗 URL Shortener

A modern, feature-rich URL shortener built with Flask that transforms long URLs into short, shareable links with comprehensive click tracking and analytics.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Flask](https://img.shields.io/badge/flask-v2.3.3-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Bootstrap](https://img.shields.io/badge/bootstrap-v5.1.3-purple.svg)

## ✨ Features

- **🚀 Fast URL Shortening** - Convert long URLs into short, memorable links instantly
- **📊 Click Analytics** - Track clicks, timestamps, IP addresses, and user agents
- **📱 Responsive Design** - Beautiful Bootstrap UI that works on all devices
- **📋 One-Click Copy** - Copy shortened URLs to clipboard with a single click
- **🔍 Statistics Dashboard** - Detailed analytics for each shortened URL
- **🛡️ URL Validation** - Ensures only valid URLs are processed
- **🔄 Duplicate Detection** - Prevents creating multiple short URLs for the same long URL
- **🌐 RESTful API** - JSON API endpoints for programmatic access
- **📈 Real-time Tracking** - Monitor link performance with live statistics

## 🖥️ Screenshots

### Main Interface

![url_shortener screenshot](https://github.com/user-attachments/assets/edad65ef-51fe-488c-b392-ef7d60feb513)


### Statistics Dashboard


![url_shortener screenshot 2](https://github.com/user-attachments/assets/005a0bc5-8bcd-4c16-9071-8a1f1fd81b4b)

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Open your browser**
Navigate to `http://127.0.0.1:5000`

## 📁 Project Structure

```
url_shortener/
├── app.py                 # Main Flask application
├── models.py             # Database models
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── static/
│   ├── css/
│   │   └── style.css    # Custom styles
│   └── js/
│       └── script.js    # JavaScript functionality
└── templates/
    ├── base.html        # Base template
    ├── index.html       # Main page
    └── stats.html       # Statistics page
```

## 🔧 Configuration

### Environment Variables

You can customize the application using these environment variables:

```bash
export SECRET_KEY="your-secret-key-here"
export DATABASE_URL="sqlite:///database.db"
export BASE_URL="http://127.0.0.1:5000"
```

### Configuration Options

- `SHORT_URL_LENGTH`: Length of generated short codes (default: 6)
- `SQLALCHEMY_DATABASE_URI`: Database connection string
- `BASE_URL`: Base URL for your deployment

## 🛠️ API Reference

### Shorten URL
```http
POST /shorten
Content-Type: application/x-www-form-urlencoded

url=https://example.com/very-long-url
```

### Redirect to Original URL
```http
GET /{short_code}
```

### Get Statistics (JSON)
```http
GET /api/stats/{short_code}
```

**Response:**
```json
{
  "short_code": "abc123",
  "original_url": "https://example.com/very-long-url",
  "total_clicks": 42,
  "created_at": "2024-01-15T10:30:00",
  "short_url": "http://127.0.0.1:5000/abc123"
}
```

### View Statistics Page
```http
GET /stats/{short_code}
```

## 📊 Database Schema

### URL Model
| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key |
| original_url | Text | The original long URL |
| short_code | String | Unique short code |
| created_at | DateTime | Creation timestamp |
| clicks | Integer | Total click count |
| creator_ip | String | IP address of creator |

### ClickLog Model
| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key |
| url_id | Integer | Foreign key to URL |
| clicked_at | DateTime | Click timestamp |
| ip_address | String | Visitor's IP address |
| user_agent | Text | Browser user agent |
| referer | Text | Referring page |

## 🚀 Deployment

### Production Checklist

- [ ] Set strong `SECRET_KEY` environment variable
- [ ] Use PostgreSQL instead of SQLite
- [ ] Configure proper `BASE_URL`
- [ ] Set up SSL/HTTPS
- [ ] Use a WSGI server like Gunicorn
- [ ] Implement rate limiting
- [ ] Set up monitoring and logging

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "app.py"]
```

### Heroku Deployment

1. Create a `Procfile`:
```
web: gunicorn app:app
```

2. Add gunicorn to requirements:
```bash
pip install gunicorn
pip freeze > requirements.txt
```

3. Deploy:
```bash
git add .
git commit -m "Initial commit"
heroku create your-app-name
git push heroku main
```

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Features in Development

- [ ] Custom short codes
- [ ] User authentication
- [ ] Link expiration
- [ ] QR code generation
- [ ] Bulk URL shortening
- [ ] Advanced analytics
- [ ] API rate limiting
- [ ] Link preview

## 🐛 Known Issues

- SQLite may have performance limitations with high traffic
- No built-in rate limiting (recommended for production)

## 💡 Contributing Ideas

We welcome contributions! Some ideas:
- Add user authentication system
- Implement custom short codes
- Add link expiration dates
- Create advanced analytics dashboard
- Add API rate limiting
- Implement link preview feature

## 📞 Support

If you have any questions or run into issues:

1. Check the [Issues](https://github.com/yourusername/url-shortener/issues) page
2. Create a new issue with detailed information
3. Join our [Discussions](https://github.com/yourusername/url-shortener/discussions)

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework
- [Bootstrap](https://getbootstrap.com/) - UI components
- [Font Awesome](https://fontawesome.com/) - Icons
- [SQLAlchemy](https://www.sqlalchemy.org/) - Database ORM

## 📈 Statistics

![GitHub stars](https://img.shields.io/github/stars/yourusername/url-shortener?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusename/url-shortener?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/url-shortener)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/url-shortener)

---

**Made with ❤️ by Daniel

*Don't forget to star ⭐ this repository if you found it helpful!*
