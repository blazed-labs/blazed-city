"""
    A coin is a NFT (non fungable token). It represents a centrally issued security.

    ::PARAMS::
        - self
        - city = issuing city
        - thash = hash from the town which contained the bank which issued the coins
        - timestamp = Unix timestamp at time of withdraw (ex. 1643262392) [default: current timestamp]
"""
import time
import hashlib
import random

class Coin:
    def __init__(self, city, thash, timestamp = int(time.time())):
        self.city = city
        self.thash = thash
        self.timestamp = timestamp
        self.set_signature(self)
    
    ## Signature
    
    def set_signature(self):
        random.seed(self.timestamp)
        hash_str = self.city + randint(0, 1500) + self.thash
        self.signature = hashlib.md5(hash_str.encode())

    def get_signature(self):
        return self.signature