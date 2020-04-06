lista_original = [] #Cria a variável que vai receber os valores digitados.
def solicitarNum(): #Função que solicita os números ao uusário e valida se ele quer digitar mais ou nao.
    n1 = int(input('Digite os números: '))
    lista_original.insert(0, n1) # Os números digitados são inseridos na lista.
    val = int(input('Deseja digitar mais algum número? (1 - Sim/2 - Não)'))
    if val == 1:
        solicitarNum()
    elif val == 2:
        return 0
    else:
        print('Opção Inválida.')
        exit()

solicitarNum() #Chamando a função.

def calculaPares(): #Função que calcula e exibe os números pares.
    c = 0
    print('Números Pares: ')
    for x in lista_original:
        if lista_original[c] % 2 == 0:
            print(lista_original[c], end=' | ')
        c = c + 1
    print('')

def calculaImpares(): #Função que calcula e exibe os números ímpares.
    c = 0
    print('Números Ímpares: ')
    for x in lista_original:
        if lista_original[c] % 2 != 0:
            print(lista_original[c], end=' | ')
        c = c + 1

#Chamando as funções p/ calcular e exibir números pares e ímpares da lista.
calculaPares()
calculaImpares()