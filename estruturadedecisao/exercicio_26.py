# 26.Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# Álcool:

# a. até 20 litros, desconto de 3% por litro
# b. acima de 20 litros, desconto de 5% por litro

# Gasolina:

# c. até 20 litros, desconto de 4% por litro
# d. acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
# A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina
# é R$ 2,50 o preço do litro do álcool é R$ 1,90.

bomba_de_combustivel = {1: 'A-álcool', 2: 'G-gasolina', 3: 'Exit'}

while True:
    print()
    for key, value in bomba_de_combustivel.items():
        print(key, value)
    print()
    option = int(input('Escolha o tipo de combustível que vai abastecer: '))

    litros_de_combustivel = float(input('Informe a quantidade de combustível: '))

    alcool_litros_vendidos = litros_de_combustivel * 1.90

    desconto_por_litro_de_alcool = 1.90 * 0.03 * litros_de_combustivel

    desconto_por_litro_de_alcool_2 = 1.90 * 0.05 * litros_de_combustivel

    gasolina_litros_vendidos = litros_de_combustivel * 2.50

    desconto_por_litro_de_gasolina = 2.50 * 0.04 * litros_de_combustivel

    desconto_por_litro_de_gasolina_2 = 2.50 * 0.06 * litros_de_combustivel

    if option == 1:
        if 1 <= litros_de_combustivel <= 20:
            print(f'Seu desconto foi de R$ {desconto_por_litro_de_alcool:.2f}')
            print(f'Valor a ser pago -> R$ {alcool_litros_vendidos - desconto_por_litro_de_alcool:.2f}')

        elif 21 <= litros_de_combustivel <= 290:
            print(f'Seu desconto foi de R$ {desconto_por_litro_de_alcool_2:.2f}')
            print(f'Valor a ser pago -> R$ {alcool_litros_vendidos - desconto_por_litro_de_alcool_2:.2f}')

    if option == 2:
        if 1 <= litros_de_combustivel <= 20:
            print(f'Seu desconto foi de R$ {desconto_por_litro_de_gasolina:.2f}')
            print(f'Valor a ser pago -> R$ {gasolina_litros_vendidos - desconto_por_litro_de_gasolina:.2f}')

        elif 21 <= litros_de_combustivel <= 290:
            print(f'Seu desconto foi de R$ {desconto_por_litro_de_gasolina_2:.2f}')
            print(f'Valor a ser pago -> R$ {gasolina_litros_vendidos - desconto_por_litro_de_gasolina_2:.2f}')

    if option == 3:
        print('Programa encerrado!')
        break
