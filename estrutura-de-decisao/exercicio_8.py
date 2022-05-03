# 8.Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

# Forma mais curta utilizando lista.

# lista_de_produtos = []
# produto_mais_barato = 0

# for n in range(3):
#   produto = float(input('Qual o preço do produto ' + str(n + 1) + '?' + '\n'))
#   lista_de_produtos.append(produto)
#   produto_mais_barato = min(lista_de_produtos)
# print(f'O produto mais barato custa R$ {produto_mais_barato}')

# Forma mais longa!

produto_1 = float(input('Qual o preço do produto 1 ? '))
produto_2 = float(input('Qual o preço do produto 2 ? '))
produto_3 = float(input('Qual o preço do produto 3 ? '))

if produto_1 < produto_2 and produto_1 < produto_3:
    print('Você deve comprar o primeiro produto.')
elif produto_2 < produto_1 and produto_2 < produto_3:
    print('Você deve comprar o segundo produto.')
elif produto_3 < produto_2 and produto_3 < produto_1:
    print('Você deve comprar o terceiro produto.')
