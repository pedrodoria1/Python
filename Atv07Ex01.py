lista = [1, 67.2, True, "Ana Conda"]
print ("Lista:", lista)
lista.remove (True)
lista.remove (True)
print ("Nova lista:", lista)

'''No Python a variável 1 é == a True. No comando list.remove, foi solicitado a remoção na lista de UM valor que fosse
== a True e então foi excluído o primeiro valor que preenchia esse requisito. Depois, foi solicitada a exclusão de 
outro valor == a True. O próximo item que corresponde ao que foi solicitado é True variável do tipo Boolean.
Se adicionar outra linha ao código #lista.remove (True)# o programa vai dar erro, por que não achou mais nada com valor
True. Se rodar a seguinte instrução no IDLE: 
if 1==True:
    print('True')
Vais ver que o que eu escrevi procede.
'''