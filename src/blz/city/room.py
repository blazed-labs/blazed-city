"""
    A room is a configurable portion of inventories and systems within a
    building. 

    ::PARAMS::
        - self
        - num = id unique to building 
        - config = List of config items for building [ defult [] ]
        - inventories = List of inventories within the room [ default [] ]
        - systems = List of systems tied to the building [ default [] ]
"""

class Room:
    def __init__(self, num, config = [], inventories = [], systems = []):
        self.num = num
    
    ## Config

    def set_config(self, config = []):
        self.config = config
    
    def add_config(self, config):
        self.config = config
    
    def get_config(self, i = False):
        if(isinstance(i, int == True)):
            return self.config[i]
        else:
            return self.config

    ## Inventories

    def set_inventories(self, inventories = []):
        self.inventories = inventories

    def add_inventory(self, inventory):
        self.inventories.append(inventory)

    def get_inventory(self, i = False):
        if(isinstance(i, int == True)):
            return self.inventories[i]
        else:
            return self.inventories

    ## Systems

    def set_systems(self, systems = []):
        self.systems = systems

    def add_system(self, system):
        self.systems.append(system)

    def get_system(self, i = False):
        if(isinstance(i, int == True)):
            return self.systems[i]
        else:
            return self.systems
