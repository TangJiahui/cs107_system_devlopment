## func
def make_withdrawal(balance):
    def inner(withdraw):
        new_bal = balance - withdraw
        if new_bal <0:
            print("Error: withdraw amount is more than initial balance")
        else:
            return new_bal
    return inner

## Explain

print("The initial balance is passed in and never being updated in inner function, thus everytime we call inner function with withdraw amount, it withdraws from the same original initial amount")

## demo
wd = make_withdrawal(500)
wd(600)
wd(400)
wd(300)