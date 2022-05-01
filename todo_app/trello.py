import requests
import os
# import json
from flask import render_template

HOME = 'https://api.trello.com/1'

def get_boards_from_me():
    url = f'{HOME}/members/me/boards'
    response = requests.get(url,params={'fields':'name,url', 'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    return response.json()
    # return render_template('index.html', landing_image=content['hdurl'])

def get_boards_from_my_id():
    url = f"{HOME}/members/{os.getenv('MEMBERID')}/boards"
    response = requests.get(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    return response.json()
    # return render_template('index.html', landing_image=content['hdurl'])

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
    
# get_cards_in_list_from_list_id
# GET /1/lists/{id}/cards
def get_cards_in_list_from_list_id(list_id):
    url = f"{HOME}/lists/{list_id}/cards"
    response = requests.get(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    return response.json()
    
# get_card_from_card_id
# GET /1/cards/{id}
def get_card_from_card_id(card_id):
    url = f"{HOME}/cards/{card_id}"
    response = requests.get(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    return response.json()
    
# update_card_by_card_id
# PUT /1/cards/{id}
# def update_card_by_card_id(card_id):
#     url = f"{HOME}/cards/{card_id}"
#     response = requests.put(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
#     return response.json()    

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


