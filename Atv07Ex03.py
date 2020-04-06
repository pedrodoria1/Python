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
lista3 = lista1+lista2
def imprimindoLista3(lista3): #Função que valida se a lista3 tem valores repetidos. E no fim, organiza.
    l = []
    for i in lista3:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista3 = imprimindoLista3(lista3) #Imprimindo a lista 3.
print('Lista 3: ', lista3)