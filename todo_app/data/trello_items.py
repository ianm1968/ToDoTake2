import requests
import os

HOME = 'https://api.trello.com/1'

class Item:
    def __init__(self, id, name, status = 'To Do'):
        self.id = id
        self.name = name
        self.status = status
    
    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name']) 

def get_items():
        items=[]
        open_cards = get_open_cards_in_lists_from_board_id(os.getenv('BOARD_ID'));
        for list in open_cards:
            for card in list['cards']:
                item = Item.from_trello_card(card, list)
                items.append(item)            
        return items
    
def add_item(title):
        added = add_card_to_list_by_list_id(title, os.getenv('DEFAULT_TO_DO_ID'))
        return added
    
def get_item(id):
    items = get_items()
    return next((item for item in items if item.id == id), None)

def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    list_id=get_list_id_from_name(item.status)
    result = amend_card_by_id( item.id, item.name, list_id)
    return result

def delete_item(id):
        deleted = delete_card_by_card_id(id)
        return deleted
    
def get_boards_from_me():
    url = f'{HOME}/members/me/boards'
    response = requests.get(url,params={
        'fields':'name,url', 
        'key':os.getenv('API_KEY'), 
        'token':os.getenv('TOKEN')})
    return response.json()

def get_boards_from_my_id():
    url = f"{HOME}/members/{os.getenv('MEMBER_ID')}/boards"
    response = requests.get(url,params={
        'key':os.getenv('API_KEY'), 
        'token':os.getenv('TOKEN')})
    return response.json()

# get_board_from_board_id
# GET /1/boards/{id}
def get_board_from_board_id(board_id):
    url = f"{HOME}/boards/{board_id}"
    response = requests.get(url,params={
        'key':os.getenv('API_KEY'), 
        'token':os.getenv('TOKEN')})
    return response.json()


# get_lists_from_board_id
# GET /1/boards/{id}/lists
def get_lists_from_board_id(board_id):
    url = f"{HOME}/boards/{board_id}/lists"
    response = requests.get(url,params={
        'key':os.getenv('API_KEY'), 
        'token':os.getenv('TOKEN')})
    return response.json()


# get_list_from_list_id
# GET /1/lists/{id}
def get_list_from_list_id(list_id):
    url = f"{HOME}/lists/{list_id}"
    response = requests.get(url,params={
        'key':os.getenv('API_KEY'), 
        'token':os.getenv('TOKEN')})
    return response.json()
    
    
def get_open_cards_in_lists_from_board_id(board_id):
    url = f"{HOME}/boards/{board_id}/lists"
    response = requests.get(url,params={
        'key':os.getenv('API_KEY'), 
        'token':os.getenv('TOKEN'),
        'cards':'open'})
    return response.json()
        
# get_cards_in_list_from_list_id
# GET /1/lists/{id}/cards
def get_cards_in_list_from_list_id(list_id):
    url = f"{HOME}/lists/{list_id}/cards"
    response = requests.get(url,params={
        'key':os.getenv('API_KEY'), 
        'token':os.getenv('TOKEN')})
    return response.json()
    
# get_card_from_card_id
# GET /1/cards/{id}
def get_card_from_card_id(card_id):
    url = f"{HOME}/cards/{card_id}"
    response = requests.get(url,params={
        'key':os.getenv('API_KEY'), 
        'token':os.getenv('TOKEN')})
    return response.json()

# move_card_to_list
# PUT /1/cards/{cardID}?idList={listID}
def move_card_to_list(card_id, list_id):
    url = f"{HOME}/cards/{card_id}"
    response = requests.put(url,params={
        'idList':list_id,
        'key':os.getenv('API_KEY'),
        'token':os.getenv('TOKEN')})
    print (response.status_code)
    return response.status_code    

def amend_card_by_id(card_id, name, list_id):
    url = f"{HOME}/cards/{card_id}"
    response = requests.put(url,params={
        'name': name,
        'idList':list_id,
        'key':os.getenv('API_KEY'),
        'token':os.getenv('TOKEN')})
    print (response.status_code)
    return response.status_code 

# delete_card_by_card_id
# DELETE /1/cards/{id}
def delete_card_by_card_id(card_id):
    url = f"{HOME}/cards/{card_id}"
    print(url)
    response = requests.delete(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    return response.json()  
      
def add_card_to_list_by_list_id(card_name, list_id):
    url = f"{HOME}/cards"
    print(url)
    response = requests.post(url,params={
        'name':card_name,
        'idList':list_id,
        'key':os.getenv('API_KEY'),
        'token':os.getenv('TOKEN')})
    print (response.status_code)
    return response.status_code    

def get_list_id_from_name(name):
    # get lists
    # iterate to find matching id
    lists = get_lists_from_board_id(os.getenv('BOARD_ID'))
    for list in lists:
        if list['name'] == name:
            return list['id']
    return None         
    

