""" 
    A bank is a controller of finances.
    To become a bank, the town must issue it a routing number.
    The routing number consists of an md5 hashed slug, which is unique
    to the bank in its sorrounding Town.

    ::PARAMS::
        - self
        - name = Bank name (unique to sorrounding Town)
        - routing = Bank's routing number (md5 hash of bank name)
        - account_index = Incimenting number of accounts thus issued
"""

class Bank:
    def __init__(self, name, routing, account_index = 0):
        self.name = name
        self.routing = routing
        self.account_index = account_index