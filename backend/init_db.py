from flask import Flask
from user.models import db
from config import Config

def init_db():
    """Initialize the database and create all tables"""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        # Drop all existing tables
        db.drop_all()
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")

if __name__ == "__main__":
    init_db() 