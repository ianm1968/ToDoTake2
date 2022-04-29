import requests
import os
# import json
from flask import render_template

HOME = 'https://api.trello.com/1'

def get_boards_from_me():
    url = f'{HOME}/members/me/boards'
    response = requests.get(url,params={'fields':'name,url', 'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    print(response.json())
    # return render_template('index.html', landing_image=content['hdurl'])

def get_boards_from_my_id():
    url = f"{HOME}/members/{os.getenv('MEMBERID')}/boards"
    print(url)
    response = requests.get(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    print(response.json())
    # return render_template('index.html', landing_image=content['hdurl'])

# get_board_from_board_id
# GET /1/boards/{id}
def get_board_from_board_id(board_id):
    url = f"{HOME}/boards/{board_id}"
    print(url)
    response = requests.get(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    print(response.json())


# get_lists_from_board_id
# GET /1/boards/{id}/lists
def get_lists_from_board_id(board_id):
    url = f"{HOME}/boards/{board_id}/lists"
    print(url)
    response = requests.get(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    print(response.json())


# get_list_from_list_id
# GET /1/lists/{id}
def get_list_from_list_id(list_id):
    url = f"{HOME}/lists/{list_id}"
    print(url)
    response = requests.get(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    print(response.json())
    
# get_cards_in_list_from_list_id
# GET /1/lists/{id}/cards
def get_cards_in_list_from_list_id(list_id):
    url = f"{HOME}/lists/{list_id}/cards"
    print(url)
    response = requests.get(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    print(response.json())
    
# get_card_from_card_id
# GET /1/cards/{id}
def get_card_from_card_id(card_id):
    url = f"{HOME}/cards/{card_id}"
    print(url)
    response = requests.get(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    print(response.json())
    
# update_card_by_card_id
# PUT /1/cards/{id}
def update_card_by_card_id(card_id):
    url = f"{HOME}/cards/{card_id}"
    print(url)
    response = requests.put(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    print(response.json())    

# delete_card_by_card_id
# DELETE /1/cards/{id}
def delete_card_by_card_id(card_id):
    url = f"{HOME}/cards/{card_id}"
    print(url)
    response = requests.delete(url,params={'key':os.getenv('API_KEY'), 'token':os.getenv('TOKEN')})
    print(response.json())    


