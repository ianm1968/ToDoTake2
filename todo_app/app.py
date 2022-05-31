from __future__ import generator_stop
from flask import Flask,render_template,request,redirect
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items,add_item,get_item,save_item,delete_item
import os
from todo_app.models.view_model import ViewModel
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config())

def trello_due_to_python_datetime(trello_datetime):
    result = False
#     // strip date from before the 'T'
#     split_string = these_items[2].due.split('T')
#     print split_string

def validate_date(d):
    try:
        datetime.strptime(d, '%Y-%m-%dT%H:%M:%S.%fZ')
        print(str(datetime.strptime(d, '%Y-%m-%dT%H:%M:%S.%fZ')))
        return True
    except ValueError:
        return False


@app.route('/')
def index():
    print (validate_date('2022-06-01T16:12:03.390Z'))
    these_items = get_items()
    view_model = ViewModel(these_items)
    return render_template('index.html',view_model=view_model)
    
    
@app.route('/add', methods=['POST'])
def add_item_by_title():
    add_item(request.form.get('task_title'))
    return redirect('/')

@app.route('/start', methods=['POST'])
def start_item_by_id():
    id_to_start = request.form.get('task_id')
    if id_to_start != None:
        item_to_start = get_item( id_to_start )
        item_to_start.status = os.getenv('DEFAULT_DOING_NAME')
        save_item(item_to_start)
    return redirect('/')

@app.route('/complete', methods=['POST'])
def complete_item_by_id():
    id_to_complete = request.form.get('task_id')
    if id_to_complete != None:
        item_to_complete = get_item( id_to_complete )
        item_to_complete.status = os.getenv('DEFAULT_DONE_NAME')
        save_item(item_to_complete)
    return redirect('/')

@app.route('/restore', methods=['POST'])
def restore_item_by_id():
    id_to_restore = request.form.get('task_id')
    if id_to_restore != None:
        item_to_restore = get_item( id_to_restore )
        item_to_restore.status = os.getenv('DEFAULT_TO_DO_NAME')
        save_item(item_to_restore)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_item_by_id():
    id_to_delete = request.form.get('task_id')
    item_to_delete = get_item( id_to_delete )
    if id_to_delete != None:
        delete_item(id_to_delete)
    return redirect('/')





