# from todo_app.data.trello_items import Item # <<< DONT KNOW WHY I CANT IMPORT THIS WITHOUT CAUSING TEST DISCOVERY ISSUES
import pytest
from todo_app.models.view_model import ViewModel

### ADDED BECAUSE CANT IMPORT TRELLO_ITEMS
class Item:
    def __init__(self, name, status = 'To Do', desc = '', due = ''):
        self.name = name
        self.status = status
        self.desc = desc
        self.due = due

@pytest.fixture
def test_list_one_in_to_do():
    test_item = Item(name='fred',status='To Do')
    test_list=[]
    test_list.append(test_item)
    return test_list    

@pytest.fixture
def test_list_one_in_doing():
    test_item = Item(name='fred',status='Doing')
    test_list=[]
    test_list.append(test_item)
    return test_list    

@pytest.fixture
def test_list_one_in_done():
    test_item = Item(name='fred',status='Done')
    test_list=[]
    test_list.append(test_item)
    return test_list    


def test_to_do_items(test_list_one_in_to_do):
    # arrange
    test_model=ViewModel(test_list_one_in_to_do)
    # act
    test_items = test_model.to_do_items
    # assert
    assert len(test_items) == 1

def test_doing_items(test_list_one_in_doing):
    # arrange
    test_model=ViewModel(test_list_one_in_doing)
    # act
    test_items = test_model.doing_items
    # assert
    assert len(test_items) == 1


def test_done_items(test_list_one_in_done):
    # arrange
    test_model=ViewModel(test_list_one_in_done)
    # act
    test_items = test_model.done_items
    # assert
    assert len(test_items) == 1
