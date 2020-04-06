n1 = int(input('Digite um número: ')) #Solicitando o número ao usuário.
f1 = 0 #Declarando os valores iniciais da sequência, começando do 0.
f2 = 1
cont = 3 #Declarando o valor do contador que irá incrementar.
print('{}>{}'.format(f1,f2), end='')#Imprimindo os valores iniciais.
soma= 0
#Aqui a mágica acontece.
while cont<=n1:
    f3 = f1+f2
    print('>{}'.format(f3), end='')
    f1=f2
    f2=f3
    cont+=1
    soma = soma+f3+1
print(' A soma dos termos é: {}'.format(soma))