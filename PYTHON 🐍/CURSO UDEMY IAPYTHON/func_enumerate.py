# função enumerate
lista = ["abacate", "bola", "cachorro"]
for i in lista:
	print(i)

for i in range(len(lista)): # da certo mas n eh o melhor jeito
	print(i, lista[i])
	print("\n")
for i, nome in enumerate(lista): # funcao enumerate
	print(i, nome)