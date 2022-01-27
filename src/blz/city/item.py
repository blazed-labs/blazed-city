"""
    The Item is a dynamic (movable) data storage element.
    A Item is contained within spaces (as "data") or within
    the town, or inventories. 
"""

class Item:
    def __init__(self, data = ''):
        self.data = data

    def set_data(self, data):
        self.data = data
    
    def add_data(self, data):
        self.data += data

    def get_data(self):
        return self.data

    