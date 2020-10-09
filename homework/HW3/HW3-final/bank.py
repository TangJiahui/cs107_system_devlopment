from enum import Enum

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount():
    
    def __init__(self, owner, accountType: AccountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("not be able to withdraw more money than the balance of the account")
        elif amount < 0:
            raise ValueError("not be able to withdraw a negative amount from your account")
        else:
            self.balance -= amount
        
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("not be able to deposit a negative amount into your account")
        else:
            self.balance += amount

    def __str__(self):
        return "Bank Owner: {} has an Account of Type: {}".format(self.owner,self.accountType.name) 

    def __len__(self):
        return self.balance


class BankUser():
    def __init__(self, owner):
        self.owner = owner
        self.accounts = {}
    
    def addAccount(self, accountType):
        if accountType.name not in self.accounts:
            self.accounts[accountType.name] = BankAccount(self.owner, accountType)
        else:
            raise NameError("Error: There already exists such an account type")
        
    def getBalance(self, accountType):
        if accountType.name in self.accounts:
            return len(self.accounts[accountType.name])
        else:
            raise NameError("Error: No such an account type")
        
    def deposit(self, accountType, amount):
        if accountType.name not in self.accounts:
            raise NameError("Error: No such an account type")
        else:
            self.accounts[accountType.name].deposit(amount)

    def withdraw(self, accountType, amount):
        if accountType.name not in self.accounts:
            raise NameError("Error: No such an account type")
        else:
            self.accounts[accountType.name].withdraw(amount)

    def __str__(self):
        lst = [(key,len(value)) for key,value in self.accounts.items()]
        return "Bank User: {} has accounts with balance as below:".format(self.owner)+str(lst)