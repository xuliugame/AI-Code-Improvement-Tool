# Import required modules
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from openai import OpenAI
import os
from user.models import CodeHistory, db
from datetime import datetime
import re

# Create API blueprint and initialize OpenAI client
api_bp = Blueprint('api', __name__)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@api_bp.route('/optimize', methods=['POST'])
@jwt_required()
def optimize_code():
    """Optimize code using OpenAI's GPT model"""
    data = request.get_json()
    # Validate request data
    if not data or 'code' not in data or 'language' not in data:
        return jsonify({'message': 'Missing code or language'}), 400
        
    user_id = int(get_jwt_identity())
    
    try:
        # Call OpenAI API for code optimization
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": """You are a code optimization expert. Analyze the code and provide optimization suggestions following this structure:

1. Code Analysis:
   - Explain what the code does and its current structure
   - Identify potential issues and inefficiencies
   - Analyze performance (time/space complexity if relevant)

2. Optimization Suggestions:
   - Specific improvements for logic and performance
   - Better coding practices and patterns to use
   - Error handling recommendations

3. Changes Made:
   - List the key changes in the optimized version
   - Explain why these changes make the code better

4. Optimized Code:
   - Provide the improved version with clear formatting and comments

Use markdown for code blocks and keep explanations concise but informative.
IMPORTANT: Always wrap the optimized code in a code block with triple backticks."""},
                {"role": "user", "content": f"""Please analyze and optimize this {data['language']} code:

{data['code']}"""}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        optimization_response = response.choices[0].message.content
        
        # Extract optimized code from the response
        code_match = re.search(r'```(?:python)?\n([\s\S]*?)```', optimization_response)
        optimized_code = code_match.group(1).strip() if code_match else data['code']
        
        # Save optimization history to database
        history = CodeHistory(
            user_id=user_id,
            language=data['language'],
            original_code=data['code'],
            optimized_code=optimized_code,
            optimization_suggestions=optimization_response
        )
        history.save()
        
        return jsonify({
            'id': history.id,
            'optimized_code': optimized_code,
            'suggestions': optimization_response
        }), 200
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@api_bp.route('/history', methods=['GET'])
@jwt_required()
def get_history():
    """Get user's code optimization history"""
    user_id = int(get_jwt_identity())
    # Query history entries ordered by creation date (newest first)
    histories = CodeHistory.query.filter_by(user_id=user_id).order_by(CodeHistory.created_at.desc()).all()
    
    return jsonify([{
        'id': history.id,
        'original_code': history.original_code,
        'optimized_code': history.optimized_code,
        'optimization_suggestions': history.optimization_suggestions,
        'language': history.language,
        'created_at': history.created_at.isoformat()  # Send ISO format timestamp
    } for history in histories]), 200

@api_bp.route('/history/<int:history_id>', methods=['DELETE'])
@jwt_required()
def delete_history(history_id):
    """Delete a specific code optimization history entry"""
    user_id = int(get_jwt_identity())
    # Find history entry by ID and user ID
    history = CodeHistory.query.filter_by(id=history_id, user_id=user_id).first()
    
    if not history:
        return jsonify({'message': 'History not found'}), 404
    
    history.delete()
    return jsonify({'message': 'History deleted successfully'}), 200
