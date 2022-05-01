from flask import Flask,render_template,request,redirect
from todo_app import trello
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items,add_item,get_item,save_item,delete_item


app = Flask(__name__)
app.config.from_object(Config())



@app.route('/')
def index():
    my_boards = trello.get_boards_from_me()
    # print(my_boards)
    my_first_board=trello.get_board_from_board_id(my_boards[0]['id'])
    # print(my_first_board)
    my_first_board_lists=trello.get_lists_from_board_id(my_first_board['id'])
    # print(my_first_board_lists)
    my_first_board_first_list_cards=trello.get_cards_in_list_from_list_id(my_first_board_lists[0]['id'])
    # print(my_first_board_first_list_cards)
    my_first_board_first_list_first_card=trello.get_card_from_card_id(my_first_board_first_list_cards[0]['id'])
    # print(my_first_board_first_list_first_card)
    
    #move first card to last list
    num_lists = len(my_first_board_lists)
    last_list_id = my_first_board_lists[num_lists-1]['id']
    print(last_list_id)
    trello.move_card_to_list(my_first_board_first_list_first_card['id'],last_list_id)
    trello.
    
    sorted_items = sorted(get_items(), key=lambda item: item.get('status'), reverse=True)
    return render_template("index.html", to_do_list=sorted_items)
    
@app.route('/add', methods=['POST'])
def add_item_by_title():
    add_item(request.form.get('task_title'))
    return redirect('/')

@app.route('/complete', methods=['POST'])
def complete_item_by_id():
    id_to_complete = request.form.get('task_id')
    if id_to_complete != None:
        item_to_complete = get_item( id_to_complete )
        item_to_complete['status'] = 'Completed'
        save_item(item_to_complete)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_item_by_id():
    id_to_delete = request.form.get('task_id')
    print(str(id_to_delete))
    if id_to_delete != None:
        item_to_delete = get_item(id_to_delete)
        print(str(item_to_delete))
        delete_item(id_to_delete)
    return redirect('/')
# def delete_item_by_title():



