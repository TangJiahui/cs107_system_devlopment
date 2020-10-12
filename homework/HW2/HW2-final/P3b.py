## func
def make_withdrawal(balance):
	def inner(withdraw):
		balance -= withdraw
		if balance <0:
			print("Error: withdraw amount is more than initial balance")
		else:
			return balance
	return inner

## Explain

print("updating the balance inner function doesn't work. In the inner function block, variable balance's scope is within the inner function block, which is its nearest enclosing scope. Here, the reference to balance is before assignment of any value to this variable in inner function block, thus an UnboundLocalError exception is raised, meaning the name refers to a local variable that has not yet been bound to a value at the point where the name is used")

## demo
wd = make_withdrawal(500)
wd(300)
#UnboundLocalError: local variable 'balance' referenced before assignment