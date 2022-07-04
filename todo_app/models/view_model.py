from datetime import datetime
import os


class ViewModel:

    def __init__(self, items,show_all_done_is_selected = False):
         self._items = items
         self._show_all_done_is_selected = show_all_done_is_selected
    
    @property
    def items(self):
        return self._items
    
    @property
    def show_all_done_is_selected(self):
        return self._show_all_done_is_selected
    
    @show_all_done_is_selected.setter
    def show_all_done_is_selected(self,showing):
        self._show_all_done_is_selected = showing
    
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
   
    @property
    def done_today_items(self):
        todays_done_doings = []
        today = datetime.now()
        # for this_item in self.done_items:
        #     date_last_activity = datetime.strptime(this_item.dateLastActivity, '%Y-%m-%dT%H:%M:%S.%fZ')
        #     if date_last_activity.date() == today.date():
        #         todays_done_doings.append(this_item)
        for this_item in self.done_items:
            if this_item.name > 'm':
                todays_done_doings.append(this_item)
        return todays_done_doings
        
    @property
    def done_before_today_items(self): 
        older_done_doings = []
        today = datetime.now()
        # for this_item in self.items:
        #     date_last_activity = datetime.strptime(this_item.dateLastActivity, '%Y-%m-%dT%H:%M:%S.%fZ')
        #     if date_last_activity.date() < today.date():
        #         older_done_doings.append(this_item)
        for this_item in self.done_items:
            if this_item.name <= 'm':
                older_done_doings.append(this_item)
        return older_done_doings

    @property
    def should_show_all_done_items(self):
        # True if less that 5 done (any time)
        # or if the user selects to show them all   
        # or if all items are done today
        selected = self._show_all_done_is_selected
        total_count = len(self.done_items)
        return (selected or total_count<5)
    
    # toggle button enabled     

