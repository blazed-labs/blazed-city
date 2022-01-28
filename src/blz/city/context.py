"""
    A context is a state of a city.
    Wherein the City acts as a state machine,
    context is its state.
    
    ::PARAMS::
        - self
        - name = City name (unique to World)
        - world = sorrounding world network [default: root.world]
        - ledger = City ledger [Default: NULL]
        - towns = towns in City [Default: [] ]
"""

from blz.city import ledger

class Context:
    def __init__(self, name, world = "root.world", ledger = NULL, towns = []):
        self.name = name
        self.world = world
        self.set_towns(towns)
        if(ledger == NULL):
            self.set_ledger(Ledger(name))

    ## Towns

    def set_towns(self, towns = []):
        self.towns = towns
    
    def add_town(self, town):
        self.towns.append(town)

    def get_town_number():
        return self.towns.length
    
    ## Ledger
    
    def set_ledger(self, ledger):
        self.ledger = ledger
    
    ## Transaction
    
    def add_transaction(self, transaction):
        self.ledger.add_transaction(transaction)
    
    ## Account

    def add_account(self, account):
        self.ledger.add_account(account)

        

            