# Matriz de n linhas e m colunas informada pelo usuário:

def solicitandoNum(): #Método que solicita o número de linhas e colunas ao usuário.
    global n
    global m
    n = int(input("Informe o número de linhas: "))
    m = int(input("Informe o número de colunas: "))
    if m != n:
        print('Só é possível matriz quadrada. Ou seja, valores iguais.')
        solicitandoNum()
    else:
        return 1

solicitandoNum() #Chamado do método. Fiz assim para conseguir a recursividade, caso o usuário digite valores diferentes.

def fazerMatriz(): #Aqui é onde a matriz é construida, respeitando a quantidade de linhas e colunas informadas.
    global matriz
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(int(input("matriz[{}][{}] = ".format(i, j))))
        matriz.append(linha)
        print(matriz)

fazerMatriz() #Chamada do método.

#Aqui tenho um for aninhado que percorre a matriz e onde os números do índice forem iguais, ele "appenda" e
#adiciona o valor a matriz diag.

diag = []
for i in range(n):
    for j in range(n):
        if i == j:
            diag.append(matriz[i][j])

print('Diagonal Principal: {}' .format(diag))

#Aqui tenho um for aninhado que percorre a matriz e onde os números do índice respeitarem a condição, ele "appenda" e
#adiciona o valor a matriz diagsec.

diagsec = []
for i in range(n):
    for j in range(n):
        if i == n - 1 - j:
            diagsec.append(matriz[i][j])

print('Diagonal Secundária: {}' .format(diagsec))
