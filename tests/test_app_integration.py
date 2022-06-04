import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
import requests
import os

HOME = 'https://api.trello.com/1'


@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client
    
def test_get_stub(monkeypatch, client):
    # Replace call to requests.get(url) with our own function
    monkeypatch.setattr(requests, 'get', get_stub, 'params' )
    response = client.get('/')

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

def get_stub(url, params):
    test_board_id = os.environ.get('BOARD_ID')
    fake_response_data = None
    if url == f"{HOME}/boards/{test_board_id}/lists":
    # if url == f"{HOME}/boards/{test_board_id}/lists":
        fake_response_data = [{
            'id': '123abc',
            'name': 'To Do',
            'cards': [{'id': '456', 'name': 'Test card','dateLastActivity':'2022-01-31T12:59:23.999Z','desc':''}] 
            }]
    return StubResponse(fake_response_data)

