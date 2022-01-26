"""
    A plot is a collection of ajacent spaces.
"""

class Plot:
    def __init__(self, city, town, spaces = []):
        self.city = city
        self.town = town
        self.spaces = spaces