import pytest
from user.models import User, db
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_register(client):
    response = client.post('/register', 
        json={'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 201
    assert json.loads(response.data)['message'] == 'User created successfully'

def test_register_duplicate_username(client):
    # Create a user first
    response = client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 201
    
    # Try to create a user with the same username
    response = client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 400

def test_login(client):
    # Register a user first
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    
    # Test login
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'access_token' in data

def test_login_invalid_credentials(client):
    response = client.post('/login', 
        json={'username': 'wronguser', 'password': 'wrongpass'})
    assert response.status_code == 401
    assert json.loads(response.data)['message'] == 'Invalid username or password'

def test_get_user_info(client):
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
    
    # Test getting user info
    response = client.get('/user', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['username'] == 'testuser' 