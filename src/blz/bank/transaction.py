"""
    A transaction records an exchange of currency.

    ::PARAMS::
        - self
        - send_address = address of sending account
        - recipient_address = address pf receiving account
        - comment = small description of the transaction's purpose (ex. purchase of item x)
        - amount = amount of currency exchanged
        - timestamp = UNIX timestamp of the time when transaction is sent [default: current timestamp]
"""

import time
import hashlib

class Transaction:
    def __init__(self, send_address, recipient_address, comment = "", amount = 0, timestamp = int(time.time())):
        self.from_addr = send_address
        self.to_addr = recipient_address
        self.comment = comment
        self.amount = amount
        self.timestamp = timestamp
        self.set_signature(self)
    
    ## Signature

    def set_signature(self):
        hash_str = self.from_addr + "**" + self.to_addr + "**" + self.timestamp + "**" + self.amount
        self.signature = hashlib.md5(hash_str.encode())

    def check_signature(self, signature):
        if(self.signature == signature):
            return True
        else:
            return False

    