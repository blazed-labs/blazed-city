"""
    A system is like an item, wherein it has privileges, data, and functionality.
    However, unlike an item it is both completely free & mobile, and it may require 
    special licensing to operate. 
"""

class System:
    def __init__(self, data = '', methods = []):
        self.set_data(data)
        self.set_methods(methods)
    
    def set_data(self, data = ''):
        self.data = data
    
    def add_data(self, data):
        self.data += data
    
    def set_methods(self, methods = []):
        self.methods = methods

    def add_method(self, method):
        self.methods.append(method)