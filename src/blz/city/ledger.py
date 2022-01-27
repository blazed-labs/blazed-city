"""
    A ledger records transactions, and at any given time,
    holds the current "state" of an economy.
"""

class Ledger:
    def __init__(self, accounts = [], transactions = []):
        self.set_accounts(accounts)
        self.set_transactions(transactions)

    def set_accounts(self, accounts = []):
        self.accounts = accounts
    
    def add_account(self, account):
        self.accounts.append(account)

    def set_transactions(self, transactions = []):
        self.transactions = transactions

    def add_transaction(self, transaction):
        self.transactions.append(transaction)