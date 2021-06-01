a = "Alessandra"
b = "Diamantino"
concatenar = a + " " + b + " "
print(concatenar.lower()) # mudar para maiúsculo
print(concatenar.upper()) # mudar para minúsculo
# se eu imprimir concatenar normalmente, ela vai continuar normal, mas se eu fizer a variavél concatenar receber o lower ou o upper, ela será alterada :para
print(concatenar.strip()) #essa remove o espaço
print(concatenar.split()) #essa separa e transforma em uma lista :O
frase = "O rato roeu a roupa do rei de Roma"
busca = frase.find("rei") # busca a palavra e mostra a posição
print(busca)
print(frase[3:]) # mostra da posição 3 até o final
print(frase[busca:]) # de onde eu busquei lá em cima até o final
# se a string não for encontrada, é retornado -1
frase = frase.replace("do rei", "da rainha")
print(frase)