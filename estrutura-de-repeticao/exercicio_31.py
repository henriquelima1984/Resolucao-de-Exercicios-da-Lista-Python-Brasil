# 31.O Sr.Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
# Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de
# valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da
# compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para
# então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para
# registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

# Lojas Tabajara
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00

import sys
import os


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


n = 0
total = 0
option = ''
print()
print('------Lojas Tabajara------')
while True:
    n += 1
    preco_produtos = float(input('Produto ' + str(n + 0) + ': R$ '))
    total += preco_produtos

    if preco_produtos == 0:
        break

print('--------------------------')
pagamento_cliente = float(input('Recebendo dinheiro do cliente: '))

print('--------------------------')
print(f'''Total: R$ {total:.2f}
Dinheiro: R$ {pagamento_cliente:.2f}
Troco: R$ {pagamento_cliente - total:.2f}''')

option = input('Deseja encerrar o caixa? [S/N]: ')

if option == 'n'.lower():
    restart_program()
else:
    print()
    print('Obrigado por comprar conosco, volte sempre!')
