import pytest
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import set_refresh_cookies
from flask_jwt_extended import unset_jwt_cookies
from flask_jwt_extended import verify_jwt_in_request
from app import app, db
from user.models import User, CodeHistory

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

def test_create_access_token():
    # Test the create_access_token function
    pass

def test_create_refresh_token():
    # Test the create_refresh_token function
    pass

def test_get_jwt():
    # Test the get_jwt function
    pass

def test_get_jwt_identity():
    # Test the get_jwt_identity function
    pass

def test_set_access_cookies():
    # Test the set_access_cookies function
    pass

def test_set_refresh_cookies():
    # Test the set_refresh_cookies function
    pass

def test_unset_jwt_cookies():
    # Test the unset_jwt_cookies function
    pass

def test_verify_jwt_in_request():
    # Test the verify_jwt_in_request function
    pass 