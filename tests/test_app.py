from todo_app.models.view_model import ViewModel

def test_to_do_items():
    # arrange
    test_model=ViewModel([{
        'id':1,
        'name': 'item1 in to do',
        'status': 'To Do'
        }])
    # act
    test_to_do_items = test_model.to_do_items
    # assert
    assert len(test_to_do_items) == 1

def test_doing_items():
    # arrange
    test_model=ViewModel([{
        'id':1,
        'name': 'item1 in to do',
        'status': 'To Do'
        }])
    # act
    test_doing_items = test_model.doing_items
    # assert
    assert len(test_doing_items) == 1

def test_done_items():
    # arrange
    test_model=ViewModel([{
        'id':1,
        'name': 'item1 in to do',
        'status': 'To Do'
        }])
    # act
    test_done_items = test_model.done_items
    # assert
    assert len(test_done_items) == 1