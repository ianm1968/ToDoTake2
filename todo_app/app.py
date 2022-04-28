from flask import Flask,render_template,request,redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items,add_item,get_item,save_item,delete_item

app = Flask(__name__)
app.config.from_object(Config())

to_do_list=[]

@app.route('/')
def index():
    global to_do_list
    to_do_list = get_items()
    to_do_list = sorted(to_do_list, key=lambda item: item.get('status'), reverse=True)
    # csv_mapping_list = sorted(csv_mapping_list, key=lambda item: item.get("Age"))
    return render_template("index.html", to_do_list=to_do_list)
    
@app.route('/add', methods=['POST'])
def add_item_by_title():
    add_item(request.form.get('task_title'))
    return redirect('/')

@app.route('/complete', methods=['POST'])
def complete_item_by_title():
    global to_do_list
    item_to_complete = request.form.get('task_title')
    for item in to_do_list:
        if item['title'] == item_to_complete:
            item['status'] = 'Completed'
            save_item(item)
            break
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_item_by_title():
    global to_do_list
    item_to_delete = request.form.get('task_title')
    for item in to_do_list:
        if item['title'] == item_to_delete:
            delete_item(item['id'])
            break
    return redirect('/')

