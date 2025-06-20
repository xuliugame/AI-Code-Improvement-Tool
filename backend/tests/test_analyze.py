import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from user.models import User, db
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['JWT_SECRET_KEY'] = 'dev-jwt-secret'  # Match the default value from app.py
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def get_token(client):
    client.post("/register", json={"username": "user1", "password": "testpass"})
    res = client.post("/login", json={"username": "user1", "password": "testpass"})
    return json.loads(res.data)["access_token"]

def test_analyze_code(client):
    token = get_token(client)
    test_code = "def add(a, b):\n    return a + b"
    response = client.post('/optimize',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'code': test_code,
            'language': 'python'
        })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'optimized_code' in data
    assert 'suggestions' in data
