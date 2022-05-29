# from todo_app.data.trello_items import Item
from todo_app.models.view_model import ViewModel

class Item:
    def __init__(self, name, status = 'To Do', desc = '', due = ''):
        self.name = name
        self.status = status
        self.desc = desc
        self.due = due
    

def test_to_do_items():
    # arrange
    test_item = Item(name='fred',status='To Do')
    test_list=[]
    test_list.append(test_item)
    test_model=ViewModel(test_list)
    # act
    test_to_do_items = test_model.to_do_items
    # assert
    assert len(test_to_do_items) == 1

def test_doing_items():
    # arrange
    test_item = Item(name='fred',status='Doing')
    test_list=[]
    test_list.append(test_item)
    test_model=ViewModel(test_list)
    # act
    test_to_do_items = test_model.doing_items
    # assert
    assert len(test_to_do_items) == 1


def test_done_items():
    # arrange
    test_item = Item(name='fred',status='Done')
    test_list=[]
    test_list.append(test_item)
    test_model=ViewModel(test_list)
    # act
    test_to_do_items = test_model.done_items
    # assert
    assert len(test_to_do_items) == 1

