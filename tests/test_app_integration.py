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

def test_add(monkeypatch, client):
    monkeypatch.setattr(requests, 'get', get_stub)
    monkeypatch.setattr(requests, 'post', post_stub)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data = {'name':'Added card name','idList':99,'key':os.getenv('API_KEY'),'token':os.getenv('TOKEN')}
    url = '/add'

    response = client.post(url, data=json.dumps(data), headers=headers)

    assert response.status_code == 200    
    # assert response.content_type == 'application/json'
    # data = {'name':'Added card name','idList':99,'key':os.getenv('API_KEY'),'token':os.getenv('TOKEN')}     
    # headers={'Content-Type': 'application/json'}
    # response = client.post('/add', data=data , headers=headers)
    # assert response.status_code == 200
    # assert 'This_card_title' in response.json()
    

# def test_delete(monkeypatch, client):
#     # Replace call to requests.delete(url) with our own function
#     monkeypatch.setattr(requests, 'delete', delete_stub)
#     # rv = client.delete.delete('MyEndPoint',
#     #                      data={'arg1', 'val'},
#     #                      headers={'Content-Type': 'application/x-www-form-urlencoded'})    
#     response = client.delete('/')

# def test_post(monkeypatch, client):
#     # Replace call to requests.put(url) with our own function
#     monkeypatch.setattr(requests, 'post', post_stub)
#     response = client.post('/')``
#     assert response.status_code == 200
    

class StubGetResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

class StubPostResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def status_code(self):
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
    return StubGetResponse(fake_response_data)

def put_stub(url, params):
    test_card_id = os.environ.get('CARD_ID')
    fake_response_data = None
    if url == f"{HOME}/cards/{test_card_id}":
        fake_response_data = requests.Response({})
        fake_response_data.status_code = 200
    return StubResponse(fake_response_data)


def delete_stub(url, params):
    test_card_id = os.environ.get('CARD_ID')
    fake_response_data = None
    if url == f"{HOME}/cards/{test_card_id}":
        fake_response_data = requests.Response()
        fake_response_data.status_code = 200
    return StubResponse(fake_response_data)

def post_stub(url, params):
    fake_response_data = None
    if url == f"{HOME}/cards":
        fake_response_data = requests.Response()
        # fake_response_data.json = {'id': '42', 'name': 'Test card','dateLastActivity':'2022-01-31T12:59:23.999Z','desc':''}
        # fake_response_data.status_code = 200
        fake_response_data.headers['Content-Type'] = 'application/json'
        # fake_response = (fake_response_data.json, fake_response_data.status_code, fake_response_data.headers)
    return fake_response_data




      


      
    

