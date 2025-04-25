# Import required modules
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Database configuration - using PostgreSQL with fallback to SQLite
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    
    # Database connection pool settings
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = 1800  # Recycle connections after 30 minutes
    
    # Disable SQLAlchemy event system for better performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Secret key for Flask session management
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")
    
    # JWT Configuration
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-jwt-secret")
    JWT_ACCESS_TOKEN_EXPIRES = 7200  # Increase token expiration to 2 hours
