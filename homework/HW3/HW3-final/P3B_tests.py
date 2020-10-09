from bank import BankUser
from bank import AccountType
from bank import BankAccount

def test_over_withdrawal(): #this test function should throw an Exception or Error 
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 10);

    ## test create multiple saving account
    try:
        user.addAccount(AccountType.SAVINGS)
    except Exception as e:
        print(e);

    ## test withdraw more than balance
    try:
        user.withdraw(AccountType.SAVINGS, 1000);
    except Exception as e:
        print(e); 

    ## test withdraw wrong account
    try:
        user.withdraw(AccountType.CHECKING, 8)
    except Exception as e:
        print(e)
    
    ## test withdraw negative amount
    try:
        user.withdraw(AccountType.SAVINGS, -10); 
    except Exception as e:
        print(e);

    ## test deposit negative amount
    try:
        user.deposit(AccountType.SAVINGS, -10);
    except Exception as e:
        print(e);
    
    ## test deposit to wrong account
    try:
        user.deposit(AccountType.CHECKING, 100);
    except Exception as e:
        print(e);
    
    ## test get balance from wrong account
    try:
        user.getBalance(AccountType.CHECKING)
    except Exception as e:
        print(e);

    ### test valid functions ###
    user.deposit(AccountType.SAVINGS, 100)
    user.withdraw(AccountType.SAVINGS, 10)
    print(user.getBalance(AccountType.SAVINGS))
    user.addAccount(AccountType.CHECKING)
    user.deposit(AccountType.CHECKING, 500)
    print(user.getBalance(AccountType.CHECKING))

    print(user)
    print(str(user))
    print(str(user.accounts[AccountType.SAVINGS.name]))
    print(str(user.accounts[AccountType.CHECKING.name]))

test_over_withdrawal();

'''
Error: There already exists such an account type
not be able to withdraw more money than the balance of the account
Error: No such an account type
not be able to withdraw a negative amount from your account
not be able to deposit a negative amount into your account
Error: No such an account type
Error: No such an account type
100
500
Bank User: Joe has accounts with balance as below:[('SAVINGS', 100), ('CHECKING', 500)]
Bank User: Joe has accounts with balance as below:[('SAVINGS', 100), ('CHECKING', 500)]
Bank Owner: Joe has an Account of Type: SAVINGS
Bank Owner: Joe has an Account of Type: CHECKING'''