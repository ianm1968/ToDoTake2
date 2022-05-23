import os
class ViewModel:
    def __init__(self, items):
         self._items = items
    
    @property
    def items(self):
        return self._items
    
    @property
    def to_do_items(self):
        to_doings = [item for item in self.items if item.status == os.getenv('DEFAULT_TO_DO_NAME')]
        return to_doings   
    
    @property
    def doing_items(self):
        doings = [item for item in self.items if item.status ==  os.getenv('DEFAULT_DOING_NAME')]
        return doings
    
    @property
    def done_items(self):
        done_doings = [item for item in self.items if item.status ==  os.getenv('DEFAULT_DONE_NAME')]
        return done_doings