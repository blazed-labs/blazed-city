"""
    The Space is a static data storage element.
    A space is found by visiting a public building or 
    establishment, made by binding many spaces together.
"""
class Space:
    def __init__(self, x, y, data = ''):
        self.x = x
        self.y = y
        self.data = data
    
    def set_data(new_data):
        self.data = new_data
    
    def add_data(new_data):
        self.data += new_data
    
    def get_data():
        return self.data