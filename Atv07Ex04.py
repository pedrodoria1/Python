lista1 = [] #Criando a variável que vai receber os valores para a lista 1.
lista2 = [] #Criando a variável que vai receber os valores para a lista 2.

def populandoListaUm(): #Função para popular a lista 1.
    l1 = int(input('Digite os valores para a lista 1: '))
    lista1.insert(0,l1)
    val = int(input('Deseja digitar mais algum número a Lista 1? (1 - Sim/2 - Não)'))
    if val == 1:
        populandoListaUm()
    elif val == 2:
        return 0
    else:
        print('Opção Inválida.')
        exit()

def populandoListaDois(): #Função para popular a lista 2.
    l2 = int(input('Digite os valores para a lista 2: '))
    lista2.insert(0,l2)
    val = int(input('Deseja digitar mais algum número a Lista 2? (1 - Sim/2 - Não)'))
    if val == 1:
        populandoListaDois()
    elif val == 2:
        return 0
    else:
        print('Opção Inválida.')
        exit()

populandoListaUm() #Chamando as funções para o usuário entrar com os valores.
populandoListaDois() #Chamando as funções para o usuário entrar com os valores.
print('Lista 1: ', lista1)
print('#'*80)
print('Lista 2: ', lista2)
print('#'*80)

def calculaIntersecao(lista1, lista2): #Função que calcula a interseção entre as listas 1 e 2.
    i = [] #Essa variável vai guardar os valores exibidos no final.
    for x in lista1: #O primeiro for percorre a lista 1.
        for y in lista2: #O segundo for percorre a lista 2.
            if x == y: #Aqui é feita a comparação, os números que derem Match aqui, serão inseridos em i.
                i.append(x) #Caso o if acima seja verdadeiro, aqui é onde o número é incrementado em i.
    return i

print('Interseção entre Lista 1 e 2: ', calculaIntersecao(lista1, lista2)) #Exibindo o resultado da função.