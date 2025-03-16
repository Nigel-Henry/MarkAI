import pytest
from unittest.mock import patch
from app import create_app

@pytest.fixture(scope='module')
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('app.routes.requests.get')
def test_google_search(mock_get, client):
    mock_get.return_value.json.return_value = {'items': []}
    
    response = client.get('/apis/google/search?q=test')
    
    assert response.status_code == 200
    assert 'items' in response.get_json()