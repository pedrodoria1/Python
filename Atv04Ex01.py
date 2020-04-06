abcissa = int(input('Informe a abcissa do ponto: ')) #Solicitando o valor do eixo das Abcissas.
ordenada = int(input('Informe a ordenada do ponto: ')) #Solicitando o valor do eixo das Ordenadas.

print('Ponto: X:{}, Y:{}'.format(abcissa,ordenada)) #Informando as coordenadas com base nos valores informados.


'''Fazendo a validação do Quadrante ou Eixo.
Pensei em fazer uma função pra quadrante e outra pra eixo, mas fiquei na dúvida se quando um ponto está no eixo, ele está ou não no quadrante.'''

if abcissa>0 and ordenada>0:
    print('Quadrante 1')
elif abcissa<0 and ordenada>0:
    print('Quadrante 2')
elif abcissa<0 and ordenada<0:
    print('Quadrante 3')
elif abcissa>0 and ordenada<0:
    print('Quadrante 4')
elif abcissa==0 and ordenada==0:
    print('Ponto situado na origem do plano cartesiano.')
elif abcissa==0 and ordenada<0:
    print('Ponto está na parte negativa do eixo Y')
elif abcissa==0 and ordenada>0:
    print('Ponto está na parte positiva do eixo Y')
elif abcissa<0 and ordenada==0:
    print('Ponto está na parte negativa do eixo X')
elif abcissa>0 and ordenada==0:
    print('Ponto está na parte positiva do eixo X')
else:
    exit()

