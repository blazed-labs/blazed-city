"""
    The Space is a static data storage element.
    A space is found by visiting a public building or 
    establishment, made by binding many spaces together.

    ::PARAMS::
        - self
        - data = data (or item/inventory) contained within the space
        - config = list of config elements pertaining to the local space
"""
class Space:
    def __init__(self, data = '', config = []):
        self.config = config
        self.data = data

    ## Config

    def set_config(self, config = []):
        self.config = config
    
    def add_config(self, config_item):
        self.config.append(config_item)
    
    def get_config(self, i = False):
        if(isinstance(i, int == True)):
            return self.config[i]
        else:
            return self.config

    ## Data
    
    def set_data(self, new_data):
        self.data = new_data
    
    def add_data(self, new_data):
        self.data += new_data
    
    def get_data(self):
        return self.data