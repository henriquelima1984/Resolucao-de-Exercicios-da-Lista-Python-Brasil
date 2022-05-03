"""
1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.

O objetivo desse programa é printar na tela a mensagem Alô Mundo!

Todos são capazes de imprimir mensagens na tela, mas aqui será feito
de 4 formas!
"""

#Posso simplesmente printar
print('Alô Mundo')

#Foi criada uma variável chamada mensagem que recebeu a string 'Alô Mundo'
mensagem = 'Alô Mundo'
print(mensagem)

#Criando uma função na qual eu posso chamá-la sem necessitar usar o print várias vezes
def mensagem():
    print('Alô Mundo')
mensagem()

#Criando uma classe e utilizando o conceito de orientação a objeto
class Mensagem:
    def __init__(self, message):
        self.message = message

    def mostrar_mensagem(self):
        return self.message

if __name__ == '__main__':
    m = Mensagem(message='Alô Mundo')
    print(Mensagem.mostrar_mensagem(m))