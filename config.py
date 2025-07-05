import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_URL = os.environ.get('BASE_URL') or 'http://127.0.0.1:5000'
    
    # URL shortening settings
    SHORT_URL_LENGTH = 6
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)
