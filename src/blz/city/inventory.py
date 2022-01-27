"""
    An inventory is a collection of items which can be inside a plot (building)
    or can be exist outside or in other objects.

    ::PARAMS::
        - self
        - items = list of items contained within the inventory
"""

class Inventory:
    def __init__(self, items = []):
        self.set_items(items)
    
    def set_items(self, items = []):
        self.items = items
    
    def add_item(self, item):
        self.items.append(item)
