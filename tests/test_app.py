# from todo_app.data.trello_items import Item # <<< DONT KNOW WHY I CANT IMPORT THIS WITHOUT CAUSING TEST DISCOVERY ISSUES
from subprocess import CompletedProcess
import pytest
from todo_app.models.view_model import ViewModel
from datetime import datetime, timedelta

### ADDED BECAUSE CANT IMPORT TRELLO_ITEMS
class Item:
    def __init__(self, name, dateLastActivity = '', status = 'To Do', desc = '', ):
        self.name = name
        self.dateLastActivity = dateLastActivity
        self.status = status
        self.desc = desc

@pytest.fixture
def board_one_in_to_do():
    test_item = Item(name='fred',status='To Do')
    test_list=[]
    test_list.append(test_item)
    return test_list    

@pytest.fixture
def board_one_in_doing():
    test_item = Item(name='fred',status='Doing')
    test_list=[]
    test_list.append(test_item)
    return test_list    

@pytest.fixture
def board_one_in_done():
    test_item = Item(name='fred',status='Done')
    test_item.dateLastActivity = '123'
    test_list=[]
    test_list.append(test_item)
    return test_list    

@pytest.fixture
def board_one_each_done_today_yesterday_last_week_tomorrow():
    test_list=[]
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    yesterday = today - timedelta(days=1)
    lastweek = today - timedelta(days=7)
    today_str = datetime.strftime(today,'%Y-%m-%dT%H:%M:%S.%fZ')
    tomorrow_str = datetime.strftime(tomorrow,'%Y-%m-%dT%H:%M:%S.%fZ')
    yesterday_str = datetime.strftime(yesterday,'%Y-%m-%dT%H:%M:%S.%fZ')
    lastweek_str = datetime.strftime(lastweek,'%Y-%m-%dT%H:%M:%S.%fZ')

    test_item = Item(name='Tom is done today', dateLastActivity = today_str, status='Done')
    test_list.append(test_item)
    test_item = Item(name='Dick is done yesterday', dateLastActivity = yesterday_str, status='Done')
    test_list.append(test_item)
    test_item = Item(name='Harry is done last week',dateLastActivity = lastweek_str, status='Done')
    test_list.append(test_item)
    test_item = Item(name='Nobody can be done tomorrow',dateLastActivity = tomorrow_str, status='Done')
    test_list.append(test_item)

    return test_list    

@pytest.fixture
def board_one_in_each():
    test_list=[]
    test_item = Item(name='Tom',status='To Do')
    test_list.append(test_item)
    test_item = Item(name='Dick',status='Doing')
    test_list.append(test_item)
    test_item = Item(name='Harry',status='Done')
    test_list.append(test_item)
    return test_list    

@pytest.fixture
def board_one_hundred_in_each():
    test_list=[]
    i = 1
    while i <= 100:
        test_item = Item(name='Tom',status='To Do')
        test_list.append(test_item)
        test_item = Item(name='Dick',status='Doing')
        test_list.append(test_item)
        test_item = Item(name='Harry',status='Done')
        test_list.append(test_item)
        i += 1
    return test_list    

@pytest.fixture
def showing_false():
    return False

@pytest.fixture
def showing_true():
    return True


def test_no_items():
    # arrange
    test_model=ViewModel([])
    # act
    to_do_items = test_model.to_do_items
    doing_items = test_model.doing_items
    done_items = test_model.done_items
    # assert
    assert len(to_do_items) == 0
    assert len(doing_items) == 0
    assert len(done_items) == 0


def test_one_in_to_do(board_one_in_to_do):
    # arrange
    test_model=ViewModel(board_one_in_to_do)
    # act
    # assert
    assert len(test_model.to_do_items) == 1
    assert len(test_model.doing_items) == 0
    assert len(test_model.done_items) == 0
 

def test_one_in_doing(board_one_in_doing):
    # arrange
    test_model=ViewModel(board_one_in_doing)
    # act
    # assert
    assert len(test_model.to_do_items) == 0
    assert len(test_model.doing_items) == 1
    assert len(test_model.done_items) == 0

def test_one_in_done(board_one_in_done):
    # arrange
    test_model=ViewModel(board_one_in_done)
    # act
    # assert
    assert len(test_model.to_do_items) == 0
    assert len(test_model.doing_items) == 0
    assert len(test_model.done_items) == 1

def test_one_in_each(board_one_in_each):
    # arrange
    test_model=ViewModel(board_one_in_each)
    # act
    # assert
    assert len(test_model.to_do_items) == 1
    assert len(test_model.doing_items) == 1
    assert len(test_model.done_items) == 1

def test_one_hundred_in_each(board_one_hundred_in_each):
    # arrange
    test_model=ViewModel(board_one_hundred_in_each)
    # act
    # assert
    assert len(test_model.to_do_items) == 100
    assert len(test_model.doing_items) == 100
    assert len(test_model.done_items) == 100

# which will keep track of if we should show all the completed items, or just the most recent ones.
def test_should_show_all_done_items(board_one_in_doing,showing_true):
    test_items=ViewModel(board_one_in_doing,showing_true)
    assert test_items.should_show_all_done_items == True

# which will return all of the tasks that have been completed today.
def test_recent_done_items(board_one_each_done_today_yesterday_last_week_tomorrow):
    test_items=ViewModel(board_one_each_done_today_yesterday_last_week_tomorrow)
    assert len(test_items.recent_done_items) == 1
    
# which will return all of the tasks that were completed before today
def test_older_done_items(board_one_each_done_today_yesterday_last_week_tomorrow):
    test_items=ViewModel(board_one_each_done_today_yesterday_last_week_tomorrow)
    assert len(test_items.older_done_items) == 2
    
