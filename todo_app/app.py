from flask import Flask,render_template,request,redirect
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items,add_item,get_item,save_item,delete_item
import os

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    sorted_items = get_items()
    # sorted_items = sorted(get_items(), key=lambda item: item.get('status'), reverse=True)
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
    if id_to_delete != None:
        delete_item(id_to_delete)
    return redirect('/')



