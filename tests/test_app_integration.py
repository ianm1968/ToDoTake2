import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
import requests
import os
from flask import Response
import json

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
    
def test_index(monkeypatch, client):
    # Replace call to requests.get(url) with our own function
    monkeypatch.setattr(requests, 'get', get_stub)
    response = client.get('/')
    assert response.status_code == 200
    assert 'Test card' in response.data.decode()

    

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data


def get_stub(url, params):
    test_board_id = os.environ.get('BOARD_ID')
    fake_response_data = None
    if url == f"{HOME}/boards/{test_board_id}/lists":
        fake_response_data = [{
            'id': '1',
            'name': os.environ.get('DEFAULT_TO_DO_NAME'),
            'cards': [{'id': '42', 'name': 'Test card','dateLastActivity':'2022-01-31T12:59:23.999Z','desc':''}] 
            },{
            'id': '2',
            'name': os.environ.get('DEFAULT_DOING_NAME'),
            'cards': [{'id': '43', 'name': 'Test card DOING','dateLastActivity':'2022-01-31T11:59:23.999Z','desc':''}] 
            },{
            'id': '3',
            'name': os.environ.get('DEFAULT_DONE_NAME'),
            'cards': [{'id': '44', 'name': 'Test card done','dateLastActivity':'2022-01-31T10:59:23.999Z','desc':''}] 
            }]
    return StubResponse(fake_response_data)



      
    

