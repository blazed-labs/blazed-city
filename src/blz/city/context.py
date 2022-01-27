"""
    A context is a state of a city.
    Wherein the City acts as a state machine,
    context is its state.
    
    ::PARAMS::
        - self
        - name = City name (unique to World)
        - ledger = City ledger [Default: NULL]
        - towns = towns in City [Default: [] ]
"""

from blz.city import ledger

class Context:
    def __init__(self, name, ledger = NULL, towns = []):
        self.name = name
        self.set_towns(towns)
        if(ledger == NULL):
            self.set_ledger(Ledger(name))

    def set_towns(self, towns = []):
        self.towns = towns
    
    def add_town(self, town):
        self.towns.append(town)

    def get_town_number():
        return self.towns.length
    
    def set_ledger(self, ledger):
        self.ledger = ledger
    
    def add_transaction(self, transaction):
        self.ledger.add_transaction(transaction)

    def add_account(self, account):
        self.ledger.add_account(account)

        

            