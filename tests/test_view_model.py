import pytest
from todo_app.models.view_model import ViewModel
from todo_app.data.trello_items import Item
from datetime import datetime, timedelta
from dotenv import load_dotenv, find_dotenv

file_path = find_dotenv('.env.test')

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv(file_path, override=True)

def trello_date_time_str( date_time):
    return datetime.strftime(date_time,'%Y-%m-%dT%H:%M:%S.%fZ')
    
def build_items(num_items, item_name, date_last_activity, status):
    this_list=[]
    # this_list.append(Item(id=0,name='fred',status='To Do'))
    for i in range(num_items):
        this_list.append(Item(0,item_name, date_last_activity, status))
    return this_list

def test_no_items():
    test_model=ViewModel([])
    assert len(test_model.to_do_items) == 0
    assert len(test_model.doing_items) == 0
    assert len(test_model.done_items) == 0

def test_one_in_to_do():
    test_model=ViewModel(build_items(1, 'fred','','To Do'))
    assert len(test_model.to_do_items) == 1
    assert test_model.to_do_items[0].status == 'To Do'
    assert len(test_model.doing_items) == 0
    assert len(test_model.done_items) == 0
 

def test_one_in_doing():
    test_model=ViewModel(build_items(1, 'fred','','Doing'))
    assert len(test_model.to_do_items) == 0
    assert len(test_model.doing_items) == 1
    assert test_model.doing_items[0].status == 'Doing'
    assert len(test_model.done_items) == 0

def test_one_in_done():
    test_model=ViewModel(build_items(1, 'fred','','Done'))
    assert len(test_model.to_do_items) == 0
    assert len(test_model.doing_items) == 0
    assert len(test_model.done_items) == 1
    assert test_model.done_items[0].status == 'Done'

def test_one_in_each():
    test_list = build_items(1, 'tom','','To Do')
    test_list += build_items(1, 'dick','','Doing')
    test_list += build_items(1, 'harry','','Done')
    test_model=ViewModel(test_list)
    assert len(test_model.done_items) == 1
    assert len(test_model.to_do_items) == 1
    assert len(test_model.doing_items) == 1
    assert test_model.to_do_items[0].status == 'To Do'
    assert test_model.doing_items[0].status == 'Doing'
    assert test_model.done_items[0].status == 'Done'
    

def test_one_hundred_in_each():
    test_list = build_items(100, 'tom','','To Do')
    test_list += build_items(100, 'dick','','Doing')
    test_list += build_items(100, 'harry','','Done')
    test_model=ViewModel(test_list)
    assert len(test_model.to_do_items) == 100
    assert len(test_model.doing_items) == 100
    assert len(test_model.done_items) == 100

def test_should_show_three_today_one_yesterday():
    today=datetime.now()
    test_list = build_items(3,'Four done today', trello_date_time_str(today), 'Done')
    test_list += build_items(1,'One done yesterday', trello_date_time_str(today - timedelta(days=1)), 'Done')
    test_items=ViewModel(test_list)
    assert test_items.should_show_all_done_items == True

def test_shouldnt_show_three_today_two_yesterday():
    today=datetime.now()
    test_list = build_items(3,'Three done today', trello_date_time_str(today), 'Done')
    test_list += build_items(2,'Two done yesterday', trello_date_time_str(today - timedelta(days=1)), 'Done')
    test_items=ViewModel(test_list)
    assert test_items.should_show_all_done_items == False

def test_shouldnt_show_four_today_one_yesterday():
    today=datetime.now()
    test_list = build_items(4,'Four done today', trello_date_time_str(today), 'Done')
    test_list += build_items(1,'One done yesterday', trello_date_time_str(today - timedelta(days=1)), 'Done')
    test_items=ViewModel(test_list)
    assert test_items.should_show_all_done_items == False

def test_should_show_all_four_done_today():
    today=datetime.now()
    test_list = build_items(4,'Four done today', trello_date_time_str(today), 'Done')
    test_items=ViewModel(test_list)
    assert test_items.should_show_all_done_items == True

def test_should_show_all_five_done_today():
    today=datetime.now()
    test_list = build_items(5,'Five done today', trello_date_time_str(today), 'Done')
    test_items=ViewModel(test_list)
    assert test_items.should_show_all_done_items == True

def test_done_today_items():
    today=datetime.now()
    test_list = build_items(1,'One done today', trello_date_time_str(today), 'Done')
    test_list += build_items(2,'Two done yesterday', trello_date_time_str(today - timedelta(days=1)), 'Done')
    test_list += build_items(3,'Three done last week', trello_date_time_str(today - timedelta(days=7)), 'Done')
    test_list += build_items(4,'Four done tomorrow', trello_date_time_str(today + timedelta(days=1)), 'Done')
    test_items=ViewModel(test_list)
    assert len(test_items.done_today_items) == 1
    

def test_done_before_today_items():
    today=datetime.now()
    test_list = build_items(1,'One done today', trello_date_time_str(today), 'Done')
    test_list += build_items(2,'Two done yesterday', trello_date_time_str(today - timedelta(days=1)), 'Done')
    test_list += build_items(3,'Three done last week', trello_date_time_str(today - timedelta(days=7)), 'Done')
    test_list += build_items(4,'Four done tomorrow', trello_date_time_str(today + timedelta(days=1)), 'Done')
    test_items=ViewModel(test_list)
    assert len(test_items.done_before_today_items) == 5
    
