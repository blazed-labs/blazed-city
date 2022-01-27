"""
    A coin is a NFT (non fungable token).

    ::PARAMS::
        - self
        - thash = hash from the town which contained the bank which issued the coins
        - tiemstamp = Unix timestamp at time of withdraw (ex. 1643262392) [default: current timestamp]
        - 
"""
import time

class Coin:
    def __init__(self, thash, timestamp = int(time.time())):
        self.thash = thash
        self.timestamp = timestamp
