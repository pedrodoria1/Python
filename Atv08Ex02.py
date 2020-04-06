
#Aqui tenho duas funções para criar a matriz, mas, sem dar ao usuário a opção de linhas e colunas como na anterior.
#O range dos laçoes de repetição são 5, sendo assim, garantimos que será uma matriz 5x5.
def fazerMatriz1():
    global matriz1
    matriz1 = []
    for i in range(5):
        linha1 = []
        for j in range(5):
            linha1.append(int(input("matriz 1[{}][{}] = ".format(i, j))))
        matriz1.append(linha1)

def fazerMatriz2():
    global matriz2
    matriz2 = []
    for i in range(5):
        linha2 = []
        for j in range(5):
            linha2.append(int(input("matriz 2[{}][{}] = ".format(i, j))))
        matriz2.append(linha2)

fazerMatriz1()
fazerMatriz2()

#Função responsável por somar os valores da matriz.
#No final da função coloquei um for para exibir os valores da matriz de forma mais "bonita".

def somarMatriz(matriz1, matriz2):
    soma = 0
    matriz3 = []
    for i in range(len(matriz1)):
        linha3 = []
        for j in range(len(matriz2)):
            soma = matriz1[i][j] + matriz2[i][j]
            linha3.append(soma)
        matriz3.append(linha3)
    for p in range(5):
        print(matriz3[p])



somarMatriz(matriz1,matriz2)