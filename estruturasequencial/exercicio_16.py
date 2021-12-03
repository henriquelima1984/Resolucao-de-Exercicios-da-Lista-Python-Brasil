#16.Faça um programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros
#quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.
# math.ceil() -->  arredonda para o número inteiro de cima mais próximo.
# math.floor()-->  arredonda para o número inteiro de baixo mais próximo.

from math import ceil

area_a_ser_pintada = float(input('Informe a área em metros quadrados: '))
litro_por_metro = 3
litros_a_serem_usados = area_a_ser_pintada / litro_por_metro
litro_por_lata = 18
qtd_de_latas_a_serem_usadas = ceil(litros_a_serem_usados / litro_por_lata)
preco_total = qtd_de_latas_a_serem_usadas * 80
print(f'Você precisa comprar {qtd_de_latas_a_serem_usadas} lata(s) de tinta de 18 litros no valor de {preco_total} R$')

#melhorando formas de importações de bibliotecas do python
