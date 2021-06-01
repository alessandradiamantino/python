dicionario = {"a": "ameixa", "b": "bola", "m": "marcus"} #chave primeiro, : é o mesmo que recebe
print(dicionario["a"]) #imprime o valor de a no caso
print("\n")
print(dicionario) #imprime tudo
print("\n")

for chave in dicionario:
	print(chave) # imprime a,b,m
	print(dicionario) # imprime os nomes
	print("\n")
for chave in dicionario:
	print(chave + ":" + dicionario[chave]) # imprime tudo, a chave e o nome
print("\n")
for i in dicionario.items():
	print(i) #tupla com chaves e valores separados
	
for i in dicionario.values(): # imprime só os nomes
	print(i)

for i in dicionario.keys(): # imprime só as chaves
	print(i)


