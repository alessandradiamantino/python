lista = ["abacaxi", "melancia", "abacate"]
lista2 = [1,2,3,4,5]
lista3 = ["marcus", 1, 4.6, False]
print(lista)
print(lista2)
print(lista3)
print("\n")
print(lista[2])
print(lista2[3])
print(lista3[0])
print("\n")
for item in lista3: #imprime 1 por 1
	print(item)

tamanho = len(lista) #mostra o tamanho da lista
print(tamanho)
print("\n")
lista.append("limao") #adiciona item na lista
print(lista)
print("\n")
if 3 in lista2: #verifica se esta na lista
	print("3 esta na lista")

del lista[2:] #remove o item do 2 ate o final (nesse caso)
print(lista)
print("\n")
lista4 = []
lista4.append("Ale")
print(lista4)