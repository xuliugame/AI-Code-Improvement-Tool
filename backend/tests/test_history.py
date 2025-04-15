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

def test_history(client):
    token = get_token(client)
    
    # Create a history record
    test_code = "def add(a, b):\n    return a + b"
    client.post('/optimize',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'code': test_code,
            'language': 'python'
        })
    
    # Get history records
    response = client.get('/history',
        headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) > 0
    assert 'original_code' in data[0]
    assert 'optimized_code' in data[0]
    
    # Delete history record
    history_id = data[0]['id']
    response = client.delete(f'/history/{history_id}',
        headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    
    # Verify the history record has been deleted
    response = client.get('/history',
        headers={'Authorization': f'Bearer {token}'})
    data = json.loads(response.data)
    assert len(data) == 0


