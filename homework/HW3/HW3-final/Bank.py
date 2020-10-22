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
            raise ValueError("Error: not be able to withdraw more money than the balance of the account")
        elif amount < 0:
            raise ValueError("Error: not be able to withdraw a negative amount from your account")
        else:
            self.balance -= amount
        
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Error: not be able to deposit a negative amount into your account")
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

def ATMSession(bankUser):
    def Interface():
        while True:
            try:
                option = int(input("Enter Option:\n1)Exit\n2)Create Account\n3)Check Balance\n4)Deposit\n5)Withdraw\n"))
                if option == 1:
                    break
                elif option>=2 and option <=5:
                    acc = int(input("Enter Option:\n1)Checking\n2)Savings\n"))
                    if option==2:
                        if acc == 1:
                            bankUser.addAccount(AccountType.CHECKING)
                            print("{} account created successfully!".format(AccountType.CHECKING.name))
                        elif acc == 2:
                            bankUser.addAccount(AccountType.SAVINGS)
                            print("{} account created successfully!".format(AccountType.SAVINGS.name))
                        else:
                            raise ValueError("Pls input account value as choices given")
                    elif option == 3:
                        if (acc == 1 and AccountType.CHECKING.name not in bankUser.accounts) or (acc==2 and AccountType.SAVINGS.name not in bankUser.accounts):
                            raise ValueError("No such an account, please create an account first")
                        elif acc == 1:
                            print("Account Balance: "+ str(bankUser.getBalance(AccountType.CHECKING)))
                        elif acc == 2:
                            print("Account Balance: "+ str(bankUser.getBalance(AccountType.SAVINGS)))
                        else:
                            raise ValueError("Pls input account value as choices given")
                    elif option == 4:
                        if (acc == 1 and AccountType.CHECKING.name not in bankUser.accounts) or (acc==2 and AccountType.SAVINGS.name not in bankUser.accounts):
                            raise ValueError("No such an account, please create an account first")
                        elif acc==1 or acc ==2:
                            amount = int(input("Enter Interger Amount, Cannot Be Negative:\n"))
                            if acc == 1:
                                bankUser.deposit(AccountType.CHECKING, amount)
                                print("Deposit {} into {} account successfully!".format(amount, AccountType.CHECKING.name))
                            elif acc == 2:
                                bankUser.deposit(AccountType.SAVINGS, amount)
                                print("Deposit {} into {} account successfully!".format(amount,AccountType.SAVINGS.name))
                        else:
                            raise ValueError("Pls input account value as choices given")
                    elif option == 5:
                        if (acc == 1 and AccountType.CHECKING.name not in bankUser.accounts) or (acc==2 and AccountType.SAVINGS.name not in bankUser.accounts):
                            raise ValueError("No such an account, please create an account first")
                        elif acc==1 or acc ==2:
                            amount = int(input("Enter Interger Amount, Cannot Be Negative or More Than Balance:\n"))
                            if acc == 1:
                                bankUser.withdraw(AccountType.CHECKING, amount)
                                print("Withdraw {} from {} account successfully!".format(amount, AccountType.CHECKING.name))
                            elif acc == 2:
                                bankUser.withdraw(AccountType.SAVINGS, amount)
                                print("Withdraw {} from {} account successfully!".format(amount,AccountType.SAVINGS.name))
                        else:
                            raise ValueError("Pls input account value as choices given")
                else:
                    raise ValueError("Pls input choices as options indicated (1-5)")
            except Exception as e:
                print(e);
    return Interface

## test closure ##
#user = BankUser("Joe");
#interface_fn = ATMSession(user)
#interface_fn()
