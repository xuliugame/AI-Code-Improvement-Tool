from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from openai import OpenAI
import os
from user.models import CodeHistory, db

api_bp = Blueprint('api', __name__)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@api_bp.route('/optimize', methods=['POST'])
@jwt_required()
def optimize_code():
    data = request.get_json()
    if not data or 'code' not in data or 'language' not in data:
        return jsonify({'message': 'Missing code or language'}), 400
        
    user_id = int(get_jwt_identity())
    
    try:
        # Call OpenAI API for code optimization
        response = client.chat.completions.create(
            model="gpt-4.1",  # Use GPT-4.1 model
            messages=[
                {"role": "system", "content": "You are a code optimization expert."},
                {"role": "user", "content": f"Optimize the following {data['language']} code:\n\n{data['code']}"}
            ]
        )
        
        optimized_code = response.choices[0].message.content
        
        # Save to history
        history = CodeHistory(
            user_id=user_id,
            language=data['language'],
            original_code=data['code'],
            optimized_code=optimized_code,
            optimization_suggestions=optimized_code
        )
        history.save()
        
        return jsonify({
            'id': history.id,
            'optimized_code': optimized_code,
            'suggestions': optimized_code
        }), 200
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@api_bp.route('/history', methods=['GET'])
@jwt_required()
def get_history():
    user_id = int(get_jwt_identity())
    histories = CodeHistory.query.filter_by(user_id=user_id).order_by(CodeHistory.created_at.desc()).all()
    
    return jsonify([{
        'id': history.id,
        'original_code': history.original_code,
        'optimized_code': history.optimized_code,
        'optimization_suggestions': history.optimization_suggestions,
        'language': history.language,
        'created_at': history.created_at.isoformat()
    } for history in histories]), 200

@api_bp.route('/history/<int:history_id>', methods=['DELETE'])
@jwt_required()
def delete_history(history_id):
    user_id = int(get_jwt_identity())
    history = CodeHistory.query.filter_by(id=history_id, user_id=user_id).first()
    
    if not history:
        return jsonify({'message': 'History not found'}), 404
    
    history.delete()
    return jsonify({'message': 'History deleted successfully'}), 200
