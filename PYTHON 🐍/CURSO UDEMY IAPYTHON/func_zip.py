# zip
lista1 = [1, 2, 3, 4, 5]
lista2 = ["bola", "mato", "gato", "elefante", "olha"]
lista3 = ["R$ 2,00", "R$ 3,00", "n tem preço", "n tem preço", "n tem preço"]
for numero, nome, valor in zip(lista1, lista2, lista3):
	print(numero, nome, valor)