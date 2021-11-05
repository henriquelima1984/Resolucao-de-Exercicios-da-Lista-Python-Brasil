# 27.Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
# desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos
# e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

lista_de_frutas = [("morango", 2.50, 2.20), ("maçã", 1.80, 1.50)]

print(len(lista_de_frutas))
count = 0
calculo_do_produto = 0

print()
print('Mercadinho Python')
print()

while True:
    produto = input('Escolha sua opção: Morango ou Maçã?')
    print()
    for x in range(2):
        if produto.lower() == lista_de_frutas[x][0]:
            count = x

    if produto != lista_de_frutas[count][0]:
        print('Opção inválida!')
        continue

    peso = float(input('Informe o peso desejado: '))

    if 1 <= peso <= 5:
        calculo_do_produto = lista_de_frutas[count][1] * peso
        print(f'Nota Fiscal no valor de R$ {calculo_do_produto:.2f}')
        print()

    elif 5 < peso <= 8:
        calculo_do_produto = lista_de_frutas[count][2] * peso
        print(f'Nota Fiscal no valor de R$ {calculo_do_produto:.2f}')
        print()

    if peso > 8 or calculo_do_produto > 25:
        valor_integral_sem_desconto = lista_de_frutas[count][2] * peso
        calculo_do_produto = (lista_de_frutas[count][2] * peso) - ((lista_de_frutas[count][2] * peso) * 10 / 100)
        print(f'Nota fiscal no valor de R$ {valor_integral_sem_desconto:.2f}')
        print(f'Valor a ser pago com desconto R$ {calculo_do_produto:.2f}')
        print()
