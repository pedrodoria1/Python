# Inicia uma lista vazia:
print ("Lista vazia:")
lista = list (range (0))
print (lista)

# Inicia uma lista com os inteiros de 0 a 9:
print ("Lista com os inteiros de 0 a 9:")
lista = list (range (10))
print (lista)

# Inicia uma lista com os inteiros de -10 a 8 de 2 em 2:
print ("Lista com os inteiros de -10 a 8 de 2 em 2:")
lista = list (range (-10, 10, 2))
print (lista)

# Concatenação:
print ("Concatenação:")
lista1 = list (range (5))
lista2 = list (range (10, 20, 2))
lista = lista1 + lista2
print (lista)

# Concatenação usando a função chain ():
from itertools import chain
print ("Concatenação usando a função chain ():")
concat = chain (range (5), range (10, 20, 2))
lista = list (concat)
print (lista)

# Matriz:
print ("Matriz:")
matriz = []
matriz.append (list (range (3)))
matriz.append (list (range (5, 10)))
matriz.append (list (range (2, 10, 2)))
print (matriz)
for i in range (len (matriz)):
 for j in range (len (matriz[i])):
    print (matriz[i][j], end = ' ')
 print ()

 # Matriz de n linhas e m colunas informada pelo usuário:
 n = int(input("Informe o número de linhas: "))
 m = int(input("Informe o número de colunas: "))
 matriz = []
 for i in range(n):
     linha = []
     for j in range(m):
         linha.append(int(input("matriz[%d][%d] = " % (i, j))))
     matriz.append(linha)
     print(matriz)