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

def get_list_id_from_name(name):
    # get lists
    # iterate to find matching id
    lists = get_lists_from_board_id(os.getenv('BOARD_ID'))
    for list in lists:
        if list['name'] == name:
            return list['id']
    return None  

def get_lists_from_board_id(board_id):
    url = f"{HOME}/boards/{board_id}/lists"
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


def get_card_from_card_id(card_id):
    url = f"{HOME}/cards/{card_id}"
    response = requests.get(url,params={
        'key':os.getenv('API_KEY'), 
        'token':os.getenv('TOKEN')})
    return response.json()

def amend_card_by_id(card_id, name, list_id):
    url = f"{HOME}/cards/{card_id}"
    response = requests.put(url,params={
        'name': name,
        'idList':list_id,
        'key':os.getenv('API_KEY'),
        'token':os.getenv('TOKEN')})
    return response.status_code 

def delete_card_by_card_id(card_id):
    url = f"{HOME}/cards/{card_id}"
    response = requests.delete(url,params={
        'key':os.getenv('API_KEY'), 
        'token':os.getenv('TOKEN')})
    return response.json()  
      
def add_card_to_list_by_list_id(card_name, list_id):
    url = f"{HOME}/cards"
    response = requests.post(url,params={
        'name':card_name,
        'idList':list_id,
        'key':os.getenv('API_KEY'),
        'token':os.getenv('TOKEN')})
    return response.status_code    

      
    

