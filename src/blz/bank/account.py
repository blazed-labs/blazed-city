"""
    An account is a container for currency.

    An account can be addressed as follows:

        [thash]:[routing number]:[account number]

            ex:

            80f7abfd760f5fff9388092eca8b326d:2b03845a5aec50185289b7a2f749ee66:c4ca4238a0b923820dcc509a6f75849b

    ::PARAMS::
        - thash = hash from the town id where account was issued
        - routing = routing number (unique to Sorrounding Town)
        - account = account number (md5 hashed value of issuing bank's assigned account_index)
        - owner = hash of the standing account owner
        - balance = standing account balance (in coins) [default: 0]
"""

class Account:
    def __init__(self, thash, routing, account, owner, balance = 0):
        self.thash = thash
        self.routing = routing
        self.account = account
        self.set_owner(self, owner)
        self.balance = balance

    def set_owner(self, owner):
        self.owner = owner

    def get_balance(self):
        return self.balance
    
    def get_address(self):
        return self.thash + ":" + self.routing + ":" + self.account

    def deposit_coins(self, coints = []):
        for coin in coins:
            # TODO:
            # in the future,
            # we can check each
            # coin's integrity
            self.balance += 1

        # TODO:
        # Create a deposit transaction,
        # and submit it to City Ledger (CL)
        return True


    def withdraw_coins(self, amount = 0):
        status = NULL

        if(self.balance < amount):
            # ERROR:
            ## INSUF FUNDS
            status = False
        else:
            coin_list = []
            for i in range(amount):
                coin_list.append(coin(self.thash))
    
            # TODO:
            # Create a withdraw transaction,
            # and submit it to City Ledger (CL)
            status = coin_list
        
        return status