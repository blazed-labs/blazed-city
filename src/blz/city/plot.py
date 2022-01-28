"""
    A plot is a collection of ajacent spaces.
    A plot may also have a building, which provides a "silo" 
    functionality as a state machine and rules engine.
        
    ::PARAMS:: 
        - self
        - addr = address string {format: [world]//[city]//[town]//[addr]}
        - building = occupying building [default: NULL]
        - spaces = list of spaces (or single space) contained within plot 
                    * NOTE: may also contain 1 or more building(s).
"""

class Plot:
    def __init__(self, addr = "", building = NULL, spaces = []):
        self.addr = addr
        self.set_building(building)
        self.set_spaces(spaces)

    ## Address

    def generate_addr(self, world, city, town, num):
        sep = "//"
        self.addr = world + sep + city + sep + town + sep + num

    def get_addr(self):
        return self.addr
    
    ## Spaces

    def set_spaces(self, spaces = []):
        self.spaces = spaces

    def add_space(self, space):
        self.spaces.append(space)
    
    ## Building

    def set_building(self, building = NULL):
        self.building = building