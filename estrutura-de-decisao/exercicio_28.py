# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#                       Até 5 Kg          Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente.
# Se a compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
# valor do desconto e valor a pagar.

sessao_bovinos = [('file duplo', 4.90, 5.80), ('alcatra', 5.90, 6.80), ('picanha', 6.90, 7.80)]

count = 0
calcular_produto = 0
desconto_cartao_tabajara = 0

print()
print('Mercadinho Python')
print()


while True:
    produto = input('Escolha a carne desejada -> File Duplo / Alcatra / Picanha: ')
    forma_de_pagamento = input('Escolha uma opção: 1 - Dinheiro / 2 - Cartão: ')
    print()
    for x in range(3):
        if produto.lower() == sessao_bovinos[x][0]:
            count = x

    peso = float(input('Informe o peso desejado em (kg): '))

    if forma_de_pagamento == '1':
        if 0 < peso <= 5:
            calcular_produto = sessao_bovinos[count][1] * peso
            print(f'''
            Cupom Fiscal - Mercadinho Python
            tipo da carne -> {produto}
            qtd -> {peso:.2f} (kg)
            preço total -> R$ {calcular_produto:.2f}
            tipo de pagamento -> {forma_de_pagamento}
            valor do desconto -> 0.0
            ''')

        if peso > 5:
            calcular_produto = sessao_bovinos[count][2] * peso
            print(f'''
            Cupom Fiscal - Mercadinho Python
            tipo da carne -> {produto}
            qtd -> {peso:.2f} (kg)
            preço total -> R$ {calcular_produto:.2f}
            tipo de pagamento -> {forma_de_pagamento}
            valor do desconto -> 0.0
            ''')
            print()
    if forma_de_pagamento == '2':
        if 0 < peso <= 5:
            calcular_produto = sessao_bovinos[count][1] * peso
            desconto_cartao_tabajara = (sessao_bovinos[count][1] * peso) - ((sessao_bovinos[count][1] * peso) * 5/100)
            print(f'''
            Cupom Fiscal - Mercadinho Python
            tipo da carne -> {produto}
            qtd -> {peso:.2f} (kg)
            preço total -> R$ {calcular_produto:.2f}
            tipo de pagamento -> {forma_de_pagamento}
            valor com desconto -> R$ {desconto_cartao_tabajara:.2f}
            ''')

        if peso > 5:
            calcular_produto = sessao_bovinos[count][2] * peso
            desconto_cartao_tabajara = (sessao_bovinos[count][2] * peso) - ((sessao_bovinos[count][2] * peso) * 5 / 100)
            print(f'''
            Cupom Fiscal - Mercadinho Python
            tipo da carne -> {produto}
            qtd -> {peso:.2f} (kg)
            preço total -> R$ {calcular_produto:.2f}
            tipo de pagamento -> {forma_de_pagamento}
            valor com desconto -> {desconto_cartao_tabajara:.2f}
            ''')
            print()
