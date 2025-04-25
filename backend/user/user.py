# Import required modules
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .models import User, db
from datetime import timedelta
import sqlalchemy.exc

# Create authentication blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    try:
        data = request.get_json()
        
        # Validate request data
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({'message': 'Missing username or password'}), 400
        
        # Validate username length
        if len(data['username']) < 3 or len(data['username']) > 20:
            return jsonify({'message': 'Username must be between 3 and 20 characters'}), 400
        
        # Validate password length
        if len(data['password']) < 6:
            return jsonify({'message': 'Password must be at least 6 characters'}), 400
        
        # Check if username already exists
        if User.find_by_username(data['username']):
            return jsonify({'message': 'Username already exists'}), 400
        
        # Create and save new user
        user = User(username=data['username'])
        user.set_password(data['password'])
        
        try:
            user.save()
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            return jsonify({'message': 'Username already exists'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': f'Database error: {str(e)}'}), 500
        
        return jsonify({'message': 'User created successfully'}), 201
        
    except Exception as e:
        return jsonify({'message': f'Server error: {str(e)}'}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    """Authenticate user and return JWT token"""
    try:
        data = request.get_json()
        
        # Validate request data
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({'message': 'Missing username or password'}), 400
        
        # Find user and verify password
        user = User.find_by_username(data['username'])
        
        if not user or not user.check_password(data['password']):
            return jsonify({'message': 'Invalid username or password'}), 401
        
        try:
            # Create and return JWT token with extended expiration
            access_token = create_access_token(
                identity=str(user.id),
                expires_delta=timedelta(hours=2),
                fresh=True
            )
            
            return jsonify({
                'access_token': access_token,
                'user': {
                    'id': user.id,
                    'username': user.username
                }
            }), 200
            
        except Exception as e:
            return jsonify({'message': f'Token generation error: {str(e)}'}), 500
            
    except Exception as e:
        return jsonify({'message': f'Server error: {str(e)}'}), 500

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    """Get current user's profile information"""
    try:
        current_user_id = int(get_jwt_identity())
        user = db.session.get(User, current_user_id)
        
        if not user:
            return jsonify({'message': 'User not found'}), 404
        
        return jsonify({
            'id': user.id,
            'username': user.username,
            'created_at': user.created_at.isoformat()
        }), 200
        
    except ValueError:
        return jsonify({'message': 'Invalid user ID'}), 400
    except Exception as e:
        return jsonify({'message': f'Server error: {str(e)}'}), 500

@auth_bp.route('/user', methods=['GET'])
@jwt_required()
def get_user_info():
    """Alias for profile endpoint"""
    return profile()
