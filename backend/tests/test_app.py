import sys
import os
import pytest
from flask.testing import FlaskClient
from dotenv import load_dotenv

# Ensure the backend directory is in Python's path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from app import app  # Import the Flask app correctly

# Load environment variables (including OpenAI API Key)
load_dotenv()

@pytest.fixture
def client() -> FlaskClient:
    """
    Creates a test client for the Flask application.
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_analyze_endpoint(client):
    """
    Tests the /analyze endpoint with a real OpenAI API call.
    """
    response = client.post('/analyze', json={"code": "if x > 0: print(x)"})

    # Ensure the request was successful (HTTP 200)
    assert response.status_code == 200

    # Ensure the response contains JSON
    data = response.get_json()
    assert "improvements" in data

    # Ensure the returned suggestion is a string and not empty
    assert isinstance(data["improvements"], str)
    assert len(data["improvements"]) > 0
