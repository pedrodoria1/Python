#Esse foi o exercício que mais quebrei a cabeça haha.
#Tenho duas funções no início para criar as matrizes 4x4. Até ai ok, por que já tinha feito isso nos anteriores.

def fazerMatriz1():
    global matriz1
    global linha1
    matriz1 = []
    for i in range(4):
        linha1 = []
        for j in range(4):
            linha1.append(int(input('Matriz 1 [{}] [{}]: '.format(i,j))))
        matriz1.append(linha1)

def fazerMatriz2():
    global matriz2
    global linha2
    matriz2 = []
    for i in range(4):
        linha2 = []
        for j in range(4):
            linha2.append(int(input('Matriz 2 [{}] [{}]: '.format(i,j))))
        matriz2.append(linha2)

#def somaMatriz(matriz1,matriz2):

fazerMatriz1()
fazerMatriz2()

#Aqui vem a parte ordinária. Existe um for aninhado, um para adicionar os valores a variável matriz3 e outro
#para adicionar os valores a variável linha3. Um for faz a iteração dos valores no índice x (i) e outro no índice y(j).

matriz3 = []
result = 0
for i in range(4):
    linha3 = []
    for j in range(4):
        s1 = matriz1[i][0]*matriz2[0][j]
        s2 = matriz1[i][1]*matriz2[1][j]
        s3 = matriz1[i][2]*matriz2[2][j]
        s4 = matriz1[i][3]*matriz2[3][j]
        result = s1 + s2 + s3 + s4
        linha3.append(result)
    matriz3.append(linha3)
    result = 0

for linha in range(4):
    print(matriz3[linha])
