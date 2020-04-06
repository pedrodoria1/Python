from math import sqrt #Importando métodos que vou usar lá embaixo.
lista = [] #Cria a variável que vai receber os valores digitados.
def solicitarNum(): #Função que solicita os números ao uusário e valida se ele quer digitar mais ou nao.
    n1 = float(input('Digite os números: '))
    lista.insert(0, n1) # Os números digitados são inseridos na lista.
    val = int(input('Deseja digitar mais algum número? (1 - Sim/2 - Não)'))
    if val == 1:
        solicitarNum()
    elif val == 2:
        return 0
    else:
        print('Opção Inválida.')
        exit()

solicitarNum() #Chamando a função que solicita os números.

def calculaMedia(): # Função que calcula a média dos números digitados e o exibe.
    count = 0
    for x in lista:
        count = count + x
    media = count/len(lista)
    print('A soma dos elementos é: ', count)
    print('A quantidade de elementos é: ', len(lista))
    print('A média aritmética é: ', media)

calculaMedia() #Chamando a função que calcula a média aritmética dos números.

def calculaDesvio(): # Função que calcula o desvio padrão.
    count = 0
    for x in lista:
        count = count + x
    n = len(lista)
    media = count / len(lista)
    count2 = 0
    for x2 in lista:
        dp = x2-media
        dp = pow(dp, 2)
        count2 = count2 + dp
    result = count2/3
    result = sqrt(result)
    print('Desvio Padrão: ', result)

calculaDesvio() #Chamando a função que calcula o desvio padrão dos números.