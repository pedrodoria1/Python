def solicitaNumero():   # Solicitando o número ao usuário através de uma função.
    global n1
    n1 = int(input("Digite um número e descubra seu fatorial: "))

def calculaFatorial(): #Calculando o fatorial do número informado através de uma outra função.
    if n1<0:
        print('Digite um número igual ou maior que zero: ')
        solicitaNumero()
    else:
        resultado=1
        contador=1

        while contador <= n1:
            resultado *= contador
            contador += 1

        print(resultado)

#Chamando as funções.
solicitaNumero()
calculaFatorial()