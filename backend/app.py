# Import necessary libraries and modules
from dotenv import load_dotenv
load_dotenv()  # Load environment variables
from flask import Flask, jsonify
from flask_cors import CORS  # For handling cross-origin requests
from user.models import db, bcrypt  # Database models and bcrypt
from user.user import auth_bp  # User authentication blueprint
from api.openai_api import api_bp  # OpenAI API blueprint
from config import Config  # Application configuration
import os
from flask_jwt_extended import JWTManager  # JWT authentication management
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import inspect

# Create Flask application instance
app = Flask(__name__)
app.config.from_object(Config)  # Load configuration

# Initialize extensions
bcrypt.init_app(app)  # Initialize bcrypt first
db.init_app(app)  # Then initialize database

# JWT configuration
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'dev-jwt-secret')  # JWT secret key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # Token validity period (1 hour)
app.config['JWT_TOKEN_LOCATION'] = ['headers']  # Token location
app.config['JWT_HEADER_NAME'] = 'Authorization'  # Token header name
app.config['JWT_HEADER_TYPE'] = 'Bearer'  # Token type

# Configure CORS
CORS(app, resources={
    r"/*": {
        "origins": [
            "http://localhost:3000",
            "https://xuliugame.github.io"
        ],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
})

def check_table_exists(table_name):
    """Check if a table exists in the database"""
    inspector = inspect(db.engine)
    return table_name in inspector.get_table_names()

# Initialize database tables if they don't exist
def setup_database():
    """Set up the database and create tables if they don't exist"""
    with app.app_context():
        try:
            # Create database if it doesn't exist
            if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
                create_database(app.config['SQLALCHEMY_DATABASE_URI'])
                print("Database created successfully!")
                # Create all tables for new database
                db.create_all()
                print("Database tables created successfully!")
            else:
                # Check if required tables exist
                required_tables = ['users', 'code_history']
                missing_tables = [table for table in required_tables if not check_table_exists(table)]
                
                if missing_tables:
                    print(f"Creating missing tables: {', '.join(missing_tables)}")
                    db.create_all()
                    print("Missing tables created successfully!")
                else:
                    print("All required tables already exist!")
                    
        except Exception as e:
            print(f"Error setting up database: {str(e)}")
            raise

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




