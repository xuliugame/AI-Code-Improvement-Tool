import pytest
from user.models import User, CodeHistory, db, bcrypt
from app import app
import json
from datetime import timedelta

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['JWT_SECRET_KEY'] = 'dev-jwt-secret'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'
    with app.test_client() as client:
        with app.app_context():
            # Initialize bcrypt with the app
            bcrypt.init_app(app)
            # Create all database tables
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

@pytest.fixture
def auth_token(client):
    # Register and login user
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    token = json.loads(response.data)['access_token']
    return token

def test_optimize_code(client):
    # Register and login user
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    token = json.loads(response.data)['access_token']
    
    # Test code optimization
    response = client.post('/optimize',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'code': 'def add(a, b):\n    return a + b',
            'language': 'python'
        })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'optimized_code' in data
    assert 'suggestions' in data

def create_test_history(client):
    """Helper function to create a test history record and return its ID"""
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    token = json.loads(response.data)['access_token']
    
    client.post('/optimize',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'code': 'def add(a, b):\n    return a + b',
            'language': 'python'
        })
    
    response = client.get('/history',
        headers={'Authorization': f'Bearer {token}'})
    data = json.loads(response.data)
    return data[0]['id'], token

def test_get_history(client):
    # Create a history record first
    _, token = create_test_history(client)
    
    # Get history records
    response = client.get('/history',
        headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) > 0
    assert 'id' in data[0]  # Ensure the id field is returned
    assert 'original_code' in data[0]
    assert 'optimized_code' in data[0]
    assert 'optimization_suggestions' in data[0]

def test_delete_history(client):
    # Get a history record ID first
    history_id, token = create_test_history(client)
    
    # Delete history record
    response = client.delete(f'/history/{history_id}',
        headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    
    # Verify the history record has been deleted
    response = client.get('/history',
        headers={'Authorization': f'Bearer {token}'})
    data = json.loads(response.data)
    assert len(data) == 0 