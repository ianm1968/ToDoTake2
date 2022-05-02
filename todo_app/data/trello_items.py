import requests
import os
# import json

HOME = 'https://api.trello.com/1'


_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]


def parse(raw):
    # print (raw)
    # cardnames = 
    # get list
    # get all cards in list
    # parse
    # for each 
    return True

def get_items():
        # my_boards = get_boards_from_my_id()
        # my_first_board = get_board_from_board_id(my_boards[0]['id'])
        # my_boards = get_boards_from_me()
        # print(my_boards)
        # my_board=get_board_from_board_id(os.getenv('BOARDID'))
        # print(my_board)
        my_board_lists = get_lists_from_board_id(os.getenv('BOARDID'))
        # print(my_board_lists)
        # open_cards=get_cards_in_list_from_list_id(my_board_lists[0]['id'])
        open_cards = get_open_cards_in_lists_from_board_id(os.getenv('BOARDID'));
        # print(open_cards)
        parse(open_cards)
        return open_cards #DEFAULT_ITEMS.copy()
        """
        Fetches all saved items from the session.

        Returns:
            list: The list of saved items.
        """
        # my_boards = get_boards_from_me()
        # print(my_boards)
        # my_first_board=trello.get_board_from_board_id(my_boards[0]['id'])
        # # print(my_first_board)

    
def add_item(title):
        added = add_card_to_list_by_list_id(title, os.getenv('DEFAULT_TO_DO_ID'))
        print('Adding...' + str(added))
        return added
    
def get_item(id):
        return True

def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item

def delete_item(id):
        return True

def get_boards_from_me():
    url = f'{HOME}/members/me/boards'
    response = requests.get(url,params={'fields':'name,url', 'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    return response.json()

def get_boards_from_my_id():
    url = f"{HOME}/members/{os.getenv('MEMBERID')}/boards"
    response = requests.get(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    return response.json()

# get_board_from_board_id
# GET /1/boards/{id}
def get_board_from_board_id(board_id):
    url = f"{HOME}/boards/{board_id}"
    response = requests.get(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    return response.json()


# get_lists_from_board_id
# GET /1/boards/{id}/lists
def get_lists_from_board_id(board_id):
    url = f"{HOME}/boards/{board_id}/lists"
    response = requests.get(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    return response.json()


# get_list_from_list_id
# GET /1/lists/{id}
def get_list_from_list_id(list_id):
    url = f"{HOME}/lists/{list_id}"
    response = requests.get(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    return response.json()
    
    
def get_open_cards_in_lists_from_board_id(board_id):
    url = f"{HOME}/boards/{board_id}/lists"
    response = requests.get(url,params={
    'key':os.getenv('API_KEY'), 
    'token':os.getenv('TOKEN'),
    'cards':'open'
    })
    return response.json()
        
# get_cards_in_list_from_list_id
# GET /1/lists/{id}/cards
def get_cards_in_list_from_list_id(list_id):
    url = f"{HOME}/lists/{list_id}/cards"
    response = requests.get(url,params={
    'key':os.getenv('API_KEY'), 
    'token':os.getenv('TOKEN')
    })
    return response.json()
    
# get_card_from_card_id
# GET /1/cards/{id}
def get_card_from_card_id(card_id):
    url = f"{HOME}/cards/{card_id}"
    response = requests.get(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    return response.json()

# move_card_to_list
# PUT /1/cards/{cardID}?idList={listID}
def move_card_to_list(card_id, list_id):
    url = f"{HOME}/cards/{card_id}"
    response = requests.put(url,params={'idList':list_id,'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    print (response.status_code)
    return response.status_code    

# delete_card_by_card_id
# DELETE /1/cards/{id}
# def delete_card_by_card_id(card_id):
    # url = f"{HOME}/cards/{card_id}"
    # print(url)
    # response = requests.delete(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    # return response.json()  
      
def add_card_to_list_by_list_id(card_name, list_id):
    url = f"{HOME}/cards"
    print(url)
    response = requests.post(url,params={
    'name':card_name,
    'idList':list_id,
    'key':os.getenv('API_KEY'),
    'token':os.getenv('TOKEN')
    })
    
    print (response.status_code)
    return response.status_code    



