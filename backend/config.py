# Import required modules
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Database configuration - using PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:a111778838@localhost:5432/aicode_db')
    # Disable SQLAlchemy event system for better performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Secret key for Flask session management
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")
    # JWT secret key for token generation and verification
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
