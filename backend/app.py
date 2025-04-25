# Import necessary libraries and modules
from dotenv import load_dotenv
load_dotenv()  # Load environment variables
from flask import Flask, jsonify
from flask_cors import CORS  # For handling cross-origin requests
from user.models import db  # Database models
from user.user import auth_bp  # User authentication blueprint
from api.openai_api import api_bp  # OpenAI API blueprint
from config import Config  # Application configuration
import os
from flask_jwt_extended import JWTManager  # JWT authentication management
import sqlite3

# Create Flask application instance
app = Flask(__name__)
app.config.from_object(Config)  # Load configuration

# JWT configuration
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'dev-jwt-secret')  # JWT secret key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # Token validity period (1 hour)
app.config['JWT_TOKEN_LOCATION'] = ['headers']  # Token location
app.config['JWT_HEADER_NAME'] = 'Authorization'  # Token header name
app.config['JWT_HEADER_TYPE'] = 'Bearer'  # Token type

CORS(app)  # Enable cross-origin support
db.init_app(app)  # Initialize database

# Initialize database tables if they don't exist
def setup_database():
    """Set up the database and create tables if they don't exist"""
    db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')
    
    # Create the database directory if it doesn't exist
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Create tables if they don't exist
    with app.app_context():
        try:
            # Try to query the users table
            db.session.execute('SELECT 1 FROM users')
        except (sqlite3.OperationalError, Exception):
            # If the query fails, create all tables
            db.create_all()
            print("Database tables created successfully!")
        else:
            print("Database tables already exist!")

# Set up database on startup
setup_database()

# Initialize JWT manager
jwt = JWTManager(app)

# Token expiration callback function
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'message': 'The token has expired',
        'error': 'token_expired'
    }), 401

# Invalid token callback function
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'message': 'Invalid token',
        'error': str(error)
    }), 401

# Unauthorized access callback function
@jwt.unauthorized_loader
def unauthorized_callback(error):
    return jsonify({
        'message': 'Missing Authorization Header',
        'error': str(error)
    }), 401

# Token refresh required callback function
@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_payload):
    return jsonify({
        'message': 'The token is not fresh',
        'error': 'fresh_token_required'
    }), 401

# Register blueprints
app.register_blueprint(auth_bp)  # Register user authentication blueprint
app.register_blueprint(api_bp)  # Register API blueprint

# Health check route
@app.route("/")
def health_check():
    return "OK", 200

# Main program entry point
if __name__ == '__main__':
    app.run(debug=True)  # Start application in debug mode




