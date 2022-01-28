"""
    The Town is a containment and governance mechanism contained within a city. 
    A town inherits all laws from a city, but wherein there is no restriction from the city's convention,
    a town may choose to define rules and policies, to which its containing members may be subjected to.
    A town contains spaces, which are ajacent reservations of virtual real-estate. These spaces are tied (bound)
    together and given endpoint url's, and attached to deeds owned by business agents.

    ::PARAMS::
        - self
        - id = Sequential id assigned by sorrounding city, within context
        - name = Town name (unique to containing City)
        - world = containing world name
        - city = containing city name
        - banks = List of bank objects acting on/in the city [ default [] ]
        - plots = List of containing plots [ default [] ]
        - hash = hashed value of the town's id + its name (ex. 80f7abfd760f5fff9388092eca8b326d) [default: ""]

"""
import hashlib

class Town:
    def __init__(self, id, name, world, city, banks = [], plots = [], hash = ""):
        self.id = id
        self.name = name
        self.world = world
        self.city = city
        self.set_banks(banks)
        self.set_plots(plots)
        if(hash == ""):
            self.generate_hash(self)

    def set_name(self, name):
        self.name = name
    
    ## Banks

    def set_banks(self, banks = []):
        self.banks = banks

    def add_bank(self, bank):
        self.banks.append(bank)
    
    ## Plots

    def get_plot_number(self):
        return len(self.plots)

    def set_plots(self, plots = []):
        self.plots = plots

    def add_plot(self, plot):
        self.plots.append(plot)

    def create_plot(self, num, building = NULL, spaces = []):
        p = plot()
        p.generate_addr(self, self.world, self.city, self.name, num, building, spaces)
        self.add_plot(self, plot())

    ## Hashes

    def generate_hash(self):
        hash_str = self.id + self.name
        self.hash = hashlib.md5(hash_str.encode())
    
    def get_hash(self):
        return self.hash