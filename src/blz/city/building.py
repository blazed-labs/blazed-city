"""
    Building is essentially a silo of data and provisioning.
    Within a building is a series of rooms. The rooms all have
    configuration and or containing data.

    ::PARAMS::
        - self
        - config = List of config options [ default [] ]
        - rooms = List of rooms contained within the building [ default [] ]
"""

class Building:
    def __init__(self, config = [], rooms = []):
        self.set_rooms(rooms)

    ## Config
    def set_config(self, config = []):
        self.config = config

    def add_config(self, config):
        self.config.append(config)
    
    def get_config(self, i = False):
        if(isinstance(i, int == True)):
            return self.config[i]
        else:
            return self.config

    ## Rooms 

    def set_rooms(self, rooms = []):
        self.rooms = rooms
    
    def add_room(self, room):
        self.rooms.append(room)