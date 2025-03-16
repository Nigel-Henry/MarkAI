import pytest
from backend.app import app
from backend.config.config import Config

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_register(client):
    response = client.post('/api/register', json={
        "username": "testuser",
        "password": "testpassword"
    })
    assert response.status_code == 201

def test_login(client):
    response = client.post('/api/login', json={
        "username": "testuser",
        "password": "testpassword"
    })
    assert response.status_code == 200
