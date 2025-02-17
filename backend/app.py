from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/analyze": {"origins": "*"}})

@app.route('/analyze', methods=['POST'])
def analyze_code():
    data = request.get_json()
    code = data.get("code", "")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    # Instead of OpenAI, return hardcoded suggestions
    sample_suggestions = {
        "if": "Consider using a ternary operator for simple if-else conditions.",
        "for": "Use list comprehensions for better readability instead of 'for' loops.",
        "print": "Avoid print statements in production code; consider logging instead.",
        "default": "Make sure your variables are well-named and avoid redundant comments."
    }

    # Check if code contains specific keywords and return relevant advice
    for keyword, suggestion in sample_suggestions.items():
        if keyword in code:
            return jsonify({"improvements": suggestion})

    return jsonify({"improvements": sample_suggestions["default"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
