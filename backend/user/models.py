# Import required modules
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

# Initialize Bcrypt for password hashing and SQLAlchemy for database operations
bcrypt = Bcrypt()
db = SQLAlchemy()

class User(db.Model):
    """User model for storing user information and authentication"""
    __tablename__ = 'users'

    # User table columns
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    username = db.Column(db.String(80), unique=True, nullable=False)  # Unique username
    password = db.Column(db.String(255), nullable=False)  # Hashed password
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Account creation timestamp

    def save(self):
        """Save the user object to the database"""
        db.session.add(self)
        db.session.commit()

    def set_password(self, password):
        """Hash and set the user's password"""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Verify if the provided password matches the stored hash"""
        return bcrypt.check_password_hash(self.password, password)

    @classmethod
    def find_by_username(cls, username):
        """Find a user by their username"""
        return cls.query.filter_by(username=username).first()

class CodeHistory(db.Model):
    """Model for storing code optimization history"""
    __tablename__ = 'code_history'

    # Code history table columns
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to User
    original_code = db.Column(db.Text, nullable=False)  # Original code submitted
    optimized_code = db.Column(db.Text, nullable=False)  # Optimized code generated
    optimization_suggestions = db.Column(db.Text, nullable=False)  # Suggestions for optimization
    language = db.Column(db.String(50), nullable=False)  # Programming language used
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of optimization

    # Relationship with User model
    user = db.relationship('User', backref=db.backref('history', lazy=True))

    def save(self):
        """Save the code history entry to the database"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete the code history entry from the database"""
        db.session.delete(self)
        db.session.commit()
