from flask import Flask,render_template,request,redirect
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items,add_item,get_item,save_item,delete_item
import os
from todo_app.models.view_model import ViewModel
from datetime import datetime

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())




    @app.route('/')
    def index():
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

    @app.route('/restart', methods=['POST'])
    def restart_item_by_id():
        id_to_restart = request.form.get('task_id')
        if id_to_restart != None:
            item_to_restart = get_item( id_to_restart )
            item_to_restart.status = os.getenv('DEFAULT_TO_DO_NAME')
            save_item(item_to_restart)
        return redirect('/')

    @app.route('/delete', methods=['POST'])
    def delete_item_by_id():
        id_to_delete = request.form.get('task_id')
        item_to_delete = get_item( id_to_delete )
        if id_to_delete != None:
            delete_item(id_to_delete)
        return redirect('/')

    @app.route('/purge_done_before_today', methods=['POST'])
    def purge_done_before_today():
        these_items = get_items()
        view_model = ViewModel(these_items)
        for item in view_model.done_before_today_items:
            if item.id != None:
                delete_item(item.id)
        return redirect('/')
    return app






