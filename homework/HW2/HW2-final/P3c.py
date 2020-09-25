## func
def make_withdrawal(balance):
	def inner(withdraw):
		nonlocal balance
		balance -= withdraw
		if balance <0:
			print("Error: withdraw amount is more than initial balance")
		else:
			return balance
	return inner

## demo
wd = make_withdrawal(500)
wd(300)
wd(150)
