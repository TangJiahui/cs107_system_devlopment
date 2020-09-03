import math
def numbers(str, n):
	if str == "pi":
		result = 0
		for i in range(1,n+1):
			result += 1/(i**2)
		result = math.sqrt(result * 6)
	elif str == "golden":
		lst = [1,1]
		for i in range(2,n):
			lst.append(lst[i-1] + lst[i-2])
		result = lst[-1]/lst[-2]
	return result


def fib(n):
	if n==1 or n==2:
		return 1
	else:
		return fib(n-1)+fib(n-2)

def pi_exp(n):
	if n=0:
		return 0
	else:
		return pi_exp(n-1) + 1/(n**2)