"""
    A ledger records transactions, and at any given time,
    holds the current "state" of an economy.
    
    ::PARAMS::
        - self
        - city_name = Name of city (should be unique, if operating in a "universe" and/or a "world")
        - accounts = list of bank accounts in the city [ default [] ]
        - transactions = list of transactions waiting to be resolved. Once resolved, they are moved to sender & receiver's local account histories [ default [] ]

"""

class Ledger:
    def __init__(self, city_name, accounts = [], transactions = []):
        self.city = city_name
        self.set_accounts(accounts)
        self.set_transactions(transactions)
    
    ## Accounts

    def set_accounts(self, accounts = []):
        self.accounts = accounts
    
    def add_account(self, account):
        self.accounts.append(account)
    
    ## Transactions (unauthenticated)

    def set_transactions(self, transactions = []):
        self.transactions = transactions

    def add_transaction(self, transaction):
        self.transactions.append(transaction)