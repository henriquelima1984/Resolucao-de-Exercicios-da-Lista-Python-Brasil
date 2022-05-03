# 18.Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

termos = int(input('Digite a quantidade de termos: '))
soma = 0
max_value = None
min_value = None

for i in range(termos):
    x = int(input('Digite o algarismo: '))
    soma += x
    max_value = max_value if max_value is not None and max_value > x else x
    min_value = min_value if min_value is not None and min_value < x else x
print(f'''Maior valor = {max_value}
Menor valor = {min_value}
Soma dos algarismos = {soma}''')
