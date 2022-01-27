"""
    The Space is a static data storage element.
    A space is found by visiting a public building or 
    establishment, made by binding many spaces together.

    ::PARAMS::
        - self
        - x = location on the x axis
        - y = location on the y axis
        - data = data (or item/inventory) contained within the space
"""
class Space:
    def __init__(self, x, y, data = ''):
        self.x = x
        self.y = y
        self.data = data
    
    def set_data(self, new_data):
        self.data = new_data
    
    def add_data(self, new_data):
        self.data += new_data
    
    def get_data(self):
        return self.data