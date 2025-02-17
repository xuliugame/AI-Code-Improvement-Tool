import sys
import os
import pytest
from flask.testing import FlaskClient

# Ensure the backend directory is in Python's path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from app import app  # Import the Flask app after fixing the path


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
    Tests the /analyze endpoint with a sample code snippet.
    """
    response = client.post('/analyze', json={"code": "def add(a, b): return a + b"})

    # Check if the request was successful (HTTP 200)
    assert response.status_code == 200

    # Ensure the response contains the expected key
    assert "improvements" in response.json

    # Ensure AI response is a string (not empty)
    assert isinstance(response.json["improvements"], str)
    assert len(response.json["improvements"]) > 0
