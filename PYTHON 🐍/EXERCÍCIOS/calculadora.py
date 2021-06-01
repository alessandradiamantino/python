a = []
b = []
d = []
#a = int(input("Digite o primeiro numero\n"))
#b = int(input("Digite o segundo numero\n"))
print("1 - soma\n")
print("2 - subtração\n")
print("3 - multiplicação\n")
print("4 - divisão\n\n")
c = int(input(" "))
import os
os.system('clear') or None
if c == 1:
   x = 0
   while x < 5:
       d.append(int(input("Digite um número\n")))
       x += 1
       soma = 0
       for i in d:
           soma += 1
           print(soma)
          

'''elif c == 2:
	print(a - b)
	
elif c == 3:
    print( a * b)
    
else:
    try:
      print(a / b)
      
    except:
        print("Não é possível fazer a divisão\n")'''