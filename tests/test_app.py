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
    test_list=[]
    test_list.append(test_item)
    return test_list    


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


def test_these_items(board_one_in_to_do):
    # arrange
    test_model=ViewModel(board_one_in_to_do)
    # act
    # assert
    assert len(test_model.to_do_items) == 1
    assert len(test_model.doing_items) == 0
    assert len(test_model.done_items) == 0
 

def test_these_items(board_one_in_doing):
    # arrange
    test_model=ViewModel(board_one_in_doing)
    # act
    # assert
    assert len(test_model.to_do_items) == 0
    assert len(test_model.doing_items) == 1
    assert len(test_model.done_items) == 0

def test_these_items(board_one_in_done):
    # arrange
    test_model=ViewModel(board_one_in_done)
    # act
    # assert
    assert len(test_model.to_do_items) == 0
    assert len(test_model.doing_items) == 0
    assert len(test_model.done_items) == 1

