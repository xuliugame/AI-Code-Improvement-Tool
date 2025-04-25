from flask import Flask
from user.models import db
from config import Config
import click

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app

@click.group()
def cli():
    """Database management commands"""
    pass

@cli.command()
def init():
    """Initialize the database and create all tables"""
    app = create_app()
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")

@cli.command()
def reset():
    """Reset the database by dropping all tables and recreating them"""
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Database has been reset successfully!")

@cli.command()
def drop():
    """Drop all database tables"""
    app = create_app()
    with app.app_context():
        db.drop_all()
        print("All database tables have been dropped!")

if __name__ == "__main__":
    cli() 