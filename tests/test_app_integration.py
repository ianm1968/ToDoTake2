import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
import requests

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
    monkeypatch.setattr(requests, 'get', get_stub)
    response = client.get('/')

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

def get_stub(url, params):
    # test_board_id = os.environ.get('BOARD_ID')
    # if url == f"{HOME}/boards/{test_board_id}/lists":
    fake_response_data = [{
        'id': '123abc',
        'name': 'To Do',
        'cards': [{'id': '456', 'name': 'Test card','dateLastActivity':'2022-01-31T12:59:23.999Z','desc':''}] 
        }]
    return StubResponse(fake_response_data)

# def get_member_id_from_name(name):
#     fake_response_data = None
#     url = f"{HOME}/members/{name}":
        
#     response = requests.get(url,params={
#         'key':os.getenv('API_KEY'), 
#         'token':os.getenv('TOKEN')})
#     return response.json()['id']

# def get_lists_from_board_id(board_id):
#     fake_response_data = None
#     url = f"{HOME}/boards/{board_id}/lists"
#     response = requests.get(url,params={
#         'key':os.getenv('API_KEY'), 
#         'token':os.getenv('TOKEN')})
#     return response.json()

# def get_open_cards_in_lists_from_board_id(board_id):
#     fake_response_data = None
#     url = f"{HOME}/boards/{board_id}/lists"
#     response = requests.get(url,params={
#         'key':os.getenv('API_KEY'), 
#         'token':os.getenv('TOKEN'),
#         'cards':'open'})
#     return response.json()


# def amend_card_by_id(card_id, name, list_id, desc='', due='' ):
#     fake_response_data = None
#     url = f"{HOME}/cards/{card_id}"
#     response = requests.put(url,params={
#         'name': name,
#         'idList':list_id,
#         'key':os.getenv('API_KEY'),
#         'token':os.getenv('TOKEN')})
#     return response.status_code 

# def delete_card_by_card_id(card_id):
#     fake_response_data = None
#     url = f"{HOME}/cards/{card_id}"
#     response = requests.delete(url,params={
#         'key':os.getenv('API_KEY'), 
#         'token':os.getenv('TOKEN')})
#     return response.json()  
      
# def add_card_to_list_by_list_id(card_name, list_id):
#     fake_response_data = None
#     url = f"{HOME}/cards"
#     response = requests.post(url,params={
#         'name':card_name,
#         'idList':list_id,
#         'key':os.getenv('API_KEY'),
#         'token':os.getenv('TOKEN')})
#     return response.status_code    


      
    

