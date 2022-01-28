"""
    A system is like an item, wherein it has privileges, data, and functionality.
    However, unlike an item it is both completely free & mobile, and it may require 
    special licensing to operate. 

    ::PARAMS::
        - self
        - data = data contained within the system [ default '' ]
"""

class System:
    def __init__(self, data = ''):
        self.set_data(data)

    ## Data
    
    def set_data(self, data = ''):
        self.data = data
    
    def add_data(self, data):
        self.data += data
    
