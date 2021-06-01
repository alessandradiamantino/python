"""def soma(x, y):
	print(x + y)
soma(2, 3)"""
# ou
def soma(x, y):
	return x + y
def multi(x, y):
	return x * y
s = soma(2, 3) # = 5
m = multi(3, 5) # = 15
print(soma(s, m)) #chamando recursivamente