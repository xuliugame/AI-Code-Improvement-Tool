from flask import Flask, request, jsonify
from flask_cors import CORS
from api.openai_api import optimize_code  # Ensure this import is correct

app = Flask(__name__)
CORS(app, resources={r"/analyze": {"origins": "*"}})

@app.route('/analyze', methods=['POST'])
def analyze_code():
    """
    Endpoint to analyze and improve code using OpenAI API.
    """
    data = request.get_json()
    code = data.get("code", "")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    improvements = optimize_code(code)
    return jsonify({"improvements": improvements})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

