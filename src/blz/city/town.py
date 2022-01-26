"""
    The Town is a containment and governance mechanism contained within a city. 
    A town inherits all laws from a city, but wherein there is no restriction from the city's convention,
    a town may choose to define rules and policies, to which its containing members may be subjected to.
    A town contains spaces, which are ajacent reservations of virtual real-estate. These spaces are tied (bound)
    together and given endpoint url's, and attached to deeds owned by business agents.
"""
class Town:
    def __init__(self, id, name):
        self.id = id
        self.name = name