import pytest
from todo_app.models.view_model import ViewModel
from todo_app.data.trello_items import Item
from datetime import datetime, timedelta
from dotenv import load_dotenv, find_dotenv

file_path = find_dotenv('.env.test')
load_dotenv(file_path, override=True)

@pytest.fixture
def board_one_in_to_do():
    test_list = [Item(id=0,name='fred',status='To Do')]
    return test_list    

@pytest.fixture
def board_one_in_doing():
    test_list = [Item(id=0,name='fred',status='Doing')]
    return test_list    

@pytest.fixture
def board_one_in_done():
    test_list = [Item(id=0,name='fred',status='Done')]
    return test_list    

@pytest.fixture
def board_done_three_today_one_yesterday():
    today=datetime.now()
    yesterday=today-timedelta(days=1)
    today_str = datetime.strftime(today,'%Y-%m-%dT%H:%M:%S.%fZ')
    yesterday_str = datetime.strftime(yesterday,'%Y-%m-%dT%H:%M:%S.%fZ')
    test_list=[]
    for i in range(3):
        test_list.append(Item(id=0,name='Dick',status='Done',dateLastActivity=today_str))
    test_list.append(Item(id=0,name='Harry',status='Done',dateLastActivity=yesterday_str))
    return test_list      

@pytest.fixture
def board_done_three_today_two_yesterday():
    today=datetime.now()
    yesterday=today-timedelta(days=1)
    today_str = datetime.strftime(today,'%Y-%m-%dT%H:%M:%S.%fZ')
    yesterday_str = datetime.strftime(yesterday,'%Y-%m-%dT%H:%M:%S.%fZ')
    test_list=[]
    for i in range(3):
        test_list.append(Item(id=0,name='Dick',status='Done',dateLastActivity=today_str))
    for i in range(2):
        test_list.append(Item(id=i,name='Harry',status='Done',dateLastActivity=yesterday_str))
    return test_list      

@pytest.fixture
def board_done_four_today_one_yesterday():
    today=datetime.now()
    yesterday=today-timedelta(days=1)
    today_str = datetime.strftime(today,'%Y-%m-%dT%H:%M:%S.%fZ')
    yesterday_str = datetime.strftime(yesterday,'%Y-%m-%dT%H:%M:%S.%fZ')
    test_list=[]
    for i in range(4):
        test_list.append(Item(id=0,name='Dick',status='Done',dateLastActivity=today_str))
    test_list.append(Item(id=i,name='Harry',status='Done',dateLastActivity=yesterday_str))
    return test_list      

@pytest.fixture
def board_four_in_done_today():
    today_str = datetime.strftime(datetime.now(),'%Y-%m-%dT%H:%M:%S.%fZ')
    test_list=[]
    for i in range(4):
        test_list.append(Item(id=0,name='Harry',status='Done',dateLastActivity=today_str))
    return test_list      

@pytest.fixture
def board_five_in_done_today():
    today_str = datetime.strftime(datetime.now(),'%Y-%m-%dT%H:%M:%S.%fZ')
    test_list=[]
    for i in range(5):
        test_list.append(Item(id=0,name='Harry',status='Done',dateLastActivity=today_str))
    return test_list   

@pytest.fixture
def board_done_1today_2yesterday_3last_week_4tomorrow():
    test_list=[]
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    yesterday = today - timedelta(days=1)
    lastweek = today - timedelta(days=7)
    today_str = datetime.strftime(today,'%Y-%m-%dT%H:%M:%S.%fZ')
    yesterday_str = datetime.strftime(yesterday,'%Y-%m-%dT%H:%M:%S.%fZ')
    lastweek_str = datetime.strftime(lastweek,'%Y-%m-%dT%H:%M:%S.%fZ')
    tomorrow_str = datetime.strftime(tomorrow,'%Y-%m-%dT%H:%M:%S.%fZ')
    test_list.append(Item(id=0,name='Tom is done today', dateLastActivity = today_str, status='Done'))
    for i in range(2):
        test_list.append(Item(id=0,name='Dick is done yesterday', dateLastActivity = yesterday_str, status='Done'))
    for i in range(3):
        test_list.append(Item(id=0,name='Harry is done last week',dateLastActivity = lastweek_str, status='Done'))
    for i in range(4):
        test_item = Item(id=0,name='Nobody can be done tomorrow',dateLastActivity = tomorrow_str, status='Done')
        test_list.append(test_item)
    return test_list    

@pytest.fixture
def board_one_in_each():
    test_list=[
        Item(id=0,name='Tom',status='To Do'),
        Item(id=0,name='Dick',status='Doing'),
        Item(id=0,name='Harry',status='Done')
    ]
    return test_list    

@pytest.fixture
def board_one_hundred_in_each():
    tom_item = Item(id=0,name='Tom',status='To Do')
    dick_item = Item(id=0,name='Dick',status='Doing')
    harry_item = Item(id=0,name='Harry',status='Done')
    test_list=[]
    for i in range(100):
        test_list.append(tom_item)
        test_list.append(dick_item)
        test_list.append(harry_item)
        i += 1
    return test_list    

def test_no_items():
    test_model=ViewModel([])
    assert len(test_model.to_do_items) == 0
    assert len(test_model.doing_items) == 0
    assert len(test_model.done_items) == 0

def test_one_in_to_do(board_one_in_to_do):
    test_model=ViewModel(board_one_in_to_do)
    assert len(test_model.to_do_items) == 1
    assert test_model.to_do_items[0].status == 'To Do'
    assert len(test_model.doing_items) == 0
    assert len(test_model.done_items) == 0
 

def test_one_in_doing(board_one_in_doing):
    test_model=ViewModel(board_one_in_doing)
    assert len(test_model.to_do_items) == 0
    assert len(test_model.doing_items) == 1
    assert test_model.doing_items[0].status == 'Doing'
    assert len(test_model.done_items) == 0

def test_one_in_done(board_one_in_done):
    test_model=ViewModel(board_one_in_done)
    assert len(test_model.to_do_items) == 0
    assert len(test_model.doing_items) == 0
    assert len(test_model.done_items) == 1
    assert test_model.done_items[0].status == 'Done'

def test_one_in_each(board_one_in_each):
    test_model=ViewModel(board_one_in_each)
    assert len(test_model.to_do_items) == 1
    assert len(test_model.doing_items) == 1
    assert len(test_model.done_items) == 1
    assert test_model.to_do_items[0].status == 'To Do'
    assert test_model.doing_items[0].status == 'Doing'
    assert test_model.done_items[0].status == 'Done'
    

def test_one_hundred_in_each(board_one_hundred_in_each):
    test_model=ViewModel(board_one_hundred_in_each)
    assert len(test_model.to_do_items) == 100
    assert len(test_model.doing_items) == 100
    assert len(test_model.done_items) == 100

def test_should_show_three_today_one_yesterday(board_done_three_today_one_yesterday):
    test_items=ViewModel(board_done_three_today_one_yesterday)
    assert test_items.should_show_all_done_items == True

def test_shouldnt_show_three_today_two_yesterday(board_done_three_today_two_yesterday):
    test_items=ViewModel(board_done_three_today_two_yesterday)
    assert test_items.should_show_all_done_items == False

def test_shouldnt_show_four_today_one_yesterday(board_done_four_today_one_yesterday):
    test_items=ViewModel(board_done_four_today_one_yesterday)
    assert test_items.should_show_all_done_items == False

def test_should_show_all_four_done_today(board_four_in_done_today):
    test_items=ViewModel(board_four_in_done_today)
    assert test_items.should_show_all_done_items == True

def test_should_show_all_five_done_today(board_five_in_done_today):
    test_items=ViewModel(board_five_in_done_today)
    assert test_items.should_show_all_done_items == True

def test_done_today_items(board_done_1today_2yesterday_3last_week_4tomorrow):
    test_items=ViewModel(board_done_1today_2yesterday_3last_week_4tomorrow)
    assert len(test_items.done_today_items) == 1
    

def test_done_before_today_items(board_done_1today_2yesterday_3last_week_4tomorrow):
    test_items=ViewModel(board_done_1today_2yesterday_3last_week_4tomorrow)
    assert len(test_items.done_before_today_items) == 5
    
