"""
    A plot is a collection of ajacent spaces.

    A plot is accessed via the following address:
        [world]//[city]//[town]//[addr]

    ::PARAMS:: 
        - self
        - city = name of sorrounding city
        - town = name of sorrounding town
        - addr = address number
        - spaces = list of spaces (or single space) contained within plot 
                    * NOTE: may also contain 1 or more building(s).
"""

class Plot:
    def __init__(self, city, town, addr, spaces = []):
        self.city = city
        self.town = town
        self.addr = addr
        self.set_spaces(spaces)

    def set_spaces(self, spaces = []):
        self.spaces = spaces

    def add_space(self, space):
        self.spaces.append(space)

