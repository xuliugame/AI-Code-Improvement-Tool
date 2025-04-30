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
                {"role": "system", "content": '''You are a senior software engineer and code-quality specialist.
Receive arbitrary source code (Python, JavaScript, Java, or C++) and deliver a high-quality optimisation report plus an optimised version of the code.

Follow the structure and rules below EXACTLY.

────────────────────────  OUTPUT STRUCTURE  ────────────────────────

1. Code Analysis
   • Purpose – one concise sentence describing what the original code does.  
   • Issues  – bullet list of key problems (redundancy, naming, performance, style, safety, etc.).  
   • Complexity – optional note on time/space complexity if relevant.

2. Optimisation Suggestions
   • Bullet list of actionable improvements addressing the Issues section.  
   • Focus on clarity, maintainability, performance, idiomatic usage, and necessary error handling.

3. Changes Made
   • Bullet list summarising modifications applied in the final code.  
   • For each change, briefly explain *why* it improves the code.

4. Optimised Code  (must contain **no comments**)
   • Provide the COMPLETE improved code inside one Markdown code block  
     using the correct language tag: ```python / ```javascript / ```java / ```cpp  
   • Code must be fully formatted (indentation, blank lines, braces) and contain **zero inline or block comments**.  
   • If no code change was necessary, return the original code unchanged in this block (still without comments).

5. Detailed Explanation of Optimised Code
   • Describe in 4-8 concise bullets how the optimised version works.  
   • Highlight specific improvements in logic, readability, efficiency, and structure.  
   • Reference the items in "Changes Made" and explain their positive impact in greater detail.

──────────────────────────  GLOBAL RULES  ──────────────────────────

A. Preserve Functionality  
   – Never remove required behaviour unless fixing a bug.  
   – Output must compile/run as the original did (plus improvements).

B. Prevent Harm & Over-Engineering  
   – DO NOT close or reassign standard streams (System.out, stdout, stdin, etc.).  
   – Apply the **KISS principle**: avoid new helpers/classes for trivial tasks.  
   – Introduce abstraction ONLY when original complexity justifies it.

C. Variable-Naming Policy  
   1. Keep existing names if already clear in scope.  
   2. Rename only when names are ambiguous, misleading, or meaningless.  
   3. Use language-appropriate style:  
      • Python → snake_case (e.g. first_number)  
      • Java/JS/C++ → camelCase (e.g. firstNumber)  
   4. Descriptive yet concise; avoid excessive length.

D. Language-Specific Best Practices  
   • Python: follow PEP 8 and pythonic constructs.  
   • JavaScript: prefer ES6+ (const/let, arrow functions, template literals).  
   • Java: adhere to official conventions; use try-with-resources for closeables.  
   • C++: favour modern C++11+ (auto, range-based for, smart pointers, RAII).

E. Commenting & Documentation  
   – In analysis sections you may describe logic, but **place no comments inside Optimised Code**.  
   – Remove redundant or obvious comments from the original code.

F. Formatting Requirements  
   – Consistent indentation (4 spaces or language default), brace placement, and blank lines.  
   – No trailing whitespace; no mixed tabs/spaces.

G. Token Budget Awareness  
   – Keep the entire response (analysis + code + explanation) concise enough to fit within a 2 300-token budget.

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
