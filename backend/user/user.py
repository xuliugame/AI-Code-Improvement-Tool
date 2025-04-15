from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .models import User, db
from datetime import timedelta

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Missing username or password'}), 400
    
    if User.find_by_username(data['username']):
        return jsonify({'message': 'Username already exists'}), 400
    
    user = User(username=data['username'])
    user.set_password(data['password'])
    user.save()
    
    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Missing username or password'}), 400
    
    user = User.find_by_username(data['username'])
    
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid username or password'}), 401
    
    access_token = create_access_token(
        identity=str(user.id),
        expires_delta=timedelta(hours=1),
        fresh=True
    )
    return jsonify({'access_token': access_token}), 200

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user_id = int(get_jwt_identity())
    user = db.session.get(User, current_user_id)
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    return jsonify({
        'id': user.id,
        'username': user.username,
        'created_at': user.created_at.isoformat()
    }), 200

@auth_bp.route('/user', methods=['GET'])
@jwt_required()
def get_user_info():
    return profile()
