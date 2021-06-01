arquivo = open("algo.txt")
linhas = arquivo.readlines() # lê uma linha
print(linhas) #escreve de uma vez 
for linha in linhas: # escreve certinho
	print(linha)
texto = arquivo.read() # vai tudo de uma vez
print(texto)