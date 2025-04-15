import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import uuid
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
    username = f"user_{uuid.uuid4().hex[:8]}"
    res = client.post("/register", json={
        "username": username,
        "password": "testpass"
    })
    assert res.status_code == 201

def test_login(client):
    username = f"user_{uuid.uuid4().hex[:8]}"
    password = "testpass"
    client.post("/register", json={"username": username, "password": password})
    res = client.post("/login", json={"username": username, "password": password})
    assert res.status_code == 200


