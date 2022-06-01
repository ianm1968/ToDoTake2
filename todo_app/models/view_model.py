from datetime import datetime
import os

class ViewModel:
    def __init__(self, items):
         self._items = items
    
    @property
    def items(self):
        return self._items
    
    @property
    def to_do_items(self):
        to_doings = [this_item for this_item in self.items if this_item.status == os.getenv('DEFAULT_TO_DO_NAME')]
        return to_doings   
    
    @property
    def doing_items(self):
        doings = [this_item for this_item in self.items if this_item.status == os.getenv('DEFAULT_DOING_NAME')]
        return doings
    
    @property
    def done_items(self):
        done_doings = [this_item for this_item in self.items if this_item.status == os.getenv('DEFAULT_DONE_NAME')]
        return done_doings
    
    # which will keep track of if we should show all the completed items, or just the most recent ones.
    @property
    def should_show_all_done_items(self):
        return False

    # which will return all of the tasks that have been completed today.
    @property
    def recent_done_items(self):
        todays_done_doings = []
        today = datetime.now()
        for this_item in self.items:
            then = datetime.strptime(this_item.dateLastActivity, '%Y-%m-%dT%H:%M:%S.%fZ')
            if then.date() == today.date():
                todays_done_doings.append(this_item)
        return todays_done_doings
        
    # which will return all of the tasks that were completed before today
    @property
    def older_done_items(self): 
        older_done_doings = []
        today = datetime.now()
        for this_item in self.items:
            then = datetime.strptime(this_item.dateLastActivity, '%Y-%m-%dT%H:%M:%S.%fZ')
            if then.date() < today.date():
                older_done_doings.append(this_item)
        return older_done_doings
        
    