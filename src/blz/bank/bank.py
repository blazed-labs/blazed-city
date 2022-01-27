""" 
    A bank is a controller of finances.
    To become a bank, the town must issue it a routing number.
    The routing number consists of an md5 hashed slug, which is unique
    to the bank in its sorrounding Town.

    ::PARAMS::
        - self
        - name = Bank name (unique to sorrounding Town)
        - city = city which contains the bank name
        - thash = hash of the town which contains the bank
        - routing = Bank's routing number (md5 hash of bank name)
        - account_index = Incimenting number of accounts thus issued
"""
import hashlib

class Bank:
    def __init__(self, name, city, thash, routing, account_index = 0):
        self.name = name
        self.city = city
        self.thash = thash
        self.routing = routing
        self.account_index = account_index
    
    def new_account(self, owner, inital_balance = 0):
        self.account_index += 1
        hash_str = self.account_index + " "
        account_addr = hashlib.md5(hash_str.encode())
        return account(self.city, self.thash, self.routing, owner, inital_balance)

    