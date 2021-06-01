# list comprehension

x = [1, 2, 3, 4, 5]
y =[]

for i in x:
	y.append(i**2)

print(x)
print(y)
print("\n")
#em uma linha
#y = [valor_a_add, laço, condição]
y = [i**2 for i in x]
print("usando list comprehension")
print(x)
print(y)
print("imares")
z = [i for i in x if i%2 == 1]
print(z)