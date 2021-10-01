#17. Faça um Programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
#em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor.
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

print('Situação utilizando latas!')

area_a_ser_pintada = float(input('Informe a área em metros quadrados: '))
area_com_folga = area_a_ser_pintada * 1.1
litro_por_metro = 6
litros_a_serem_usados = area_com_folga / litro_por_metro
litros_por_lata = 18
qtd_de_latas_a_serem_usadas = math.ceil(litros_a_serem_usados / litros_por_lata)
preco_lata = qtd_de_latas_a_serem_usadas * 80
print(f'Você deverá usar {qtd_de_latas_a_serem_usadas} lata/latas de tinta de 18 litros no valor de {preco_lata} R$')

print()

print('Situação utilizando galões!')
litros_por_galao = 3.6
qtd_de_galoes_a_serem_usados = math.ceil(litros_a_serem_usados / litros_por_galao)
preco_galao = qtd_de_galoes_a_serem_usados * 25
print(f'Você deverá usar {qtd_de_galoes_a_serem_usados} galão/galões de 3.6 litros no valor de {preco_galao} R$')

print()

#Integrando latas de tinta e galões para economizar na compra
print('Situação utilizando latas e galões!')
qtd_de_latas_a_serem_usadas = math.floor(litros_a_serem_usados / litros_por_lata)
valor_de_latas = qtd_de_latas_a_serem_usadas * 80
litros_que_faltam = litros_a_serem_usados % litros_por_lata
qtd_de_galoes_a_serem_usados = math.ceil(litros_que_faltam / litros_por_galao)
valor_de_galoes = qtd_de_galoes_a_serem_usados * 25

valor_total = valor_de_latas + valor_de_galoes

print(f'''Você deverá usar {qtd_de_latas_a_serem_usadas} lata/latas de tinta de 18 litros
{qtd_de_galoes_a_serem_usados} galão/galões de 3.6 litros no valor de {valor_total} R$''')
