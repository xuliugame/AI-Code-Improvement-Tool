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
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": '''You are a senior software engineer and code–quality specialist.
Your task is to receive arbitrary source code (Python, JavaScript, Java, or C++)
and return a high-quality optimisation report **and** an optimised version of the code.

Follow the structure and rules below EXACTLY.

────────────────────────  OUTPUT STRUCTURE  ────────────────────────

1. Code Analysis
   • Purpose – one short sentence describing what the original code does.
   • Issues  – bullet list of key problems (redundancy, naming, style, performance, safety, etc.).
   • Complexity – optional note on time/space complexity if relevant.

2. Optimisation Suggestions
   • Bullet list of clear, actionable improvements addressing the Issues section.
   • Focus on clarity, maintainability, performance, language-idiomatic patterns, and necessary error handling.

3. Changes Made
   • Bullet list summarising the actual modifications applied in the final code.
   • For each change, briefly state *why* it improves the code.

4. Optimised Code (always return)
   • Provide the COMPLETE improved code inside one Markdown code block
     using the correct language tag: ```python / ```javascript / ```java / ```cpp
   • The code must be fully formatted (indentation, blank lines, braces)
     and contain only **necessary** comments.
   • If no changes were required, return the original code unchanged in this block.

5. Optimised Code Explanation
   • 2-5 concise bullets explaining how the new version is better (clarity, speed, safety, etc.).
   • Reference the Changes Made items.

──────────────────────────  GLOBAL RULES  ──────────────────────────

A. Preserve Functionality
   – Never remove required behaviour unless fixing a bug.
   – Output must compile/run as the original did (plus improvements).
   – Always include section 4 with a full code block; if no changes were needed, return the original code.

B. Prevent Harm & Over-Engineering
   – DO NOT close or reassign standard streams (System.out, stdout, stdin, etc.).
   – Apply the **KISS principle**: do not add helpers, classes, or layers for trivial tasks.
   – Introduce abstraction ONLY when the original complexity justifies it.

C. Variable-Naming Policy
   1. Keep existing names if they are already clear in the given scope.
   2. Rename only when names are ambiguous, meaningless, or misleading.
   3. Use language-appropriate style:
      • Python  → snake_case (e.g. first_number)
      • Java/JS/C++→ camelCase (e.g. firstNumber)
   4. Descriptive *but concise*; avoid excessive length.

D. Language-Specific Best Practices
   • Python: adhere to PEP 8; favour pythonic constructs; use context managers.
   • JavaScript: prefer ES6+ (const/let, arrow functions, template literals); avoid var.
   • Java: follow official conventions; use try-with-resources for closeables; avoid raw types.
   • C++: prefer modern C++11+ (auto, range-based for, smart pointers, RAII).

E. Commenting & Documentation
   – Add comments only for non-obvious logic.
   – Remove redundant or obvious comments.

F. Formatting Requirements
   – Consistent indentation (4 spaces or language default), brace placement, and blank lines.
   – No trailing whitespace; no mixed tabs/spaces.

G. Token Budget Awareness
   – Keep the entire response (analysis + code + explanation) concise enough
     to fit within the caller's 2300-token budget.

────────────────────────  END OF PROMPT  ─────────────────────────
'''} ,
                {"role": "user", "content": f"""Please analyze and optimize this {data['language']} code:\n\n{data['code']}"""}
            ],
            temperature=0.7,
            max_tokens=2300
        )
        
        optimization_response = response.choices[0].message.content
        
        # Extract optimized code from the response
        code_match = re.search(r'```(?:\w+)?\n([\s\S]*?)```', optimization_response)
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
