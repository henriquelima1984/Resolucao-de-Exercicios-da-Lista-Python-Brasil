# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input('Digite n1: '))
n2 = int(input('Digite n2: '))
n3 = float(input('Digite n3: '))

produto = (n1*2) * n2/2
soma = (n1*3) + n3
potenciacao = n3**3

print(f'O produto do dobro do primeiro com metade do segundo = {produto}')
print(f'A soma do triplo do primeiro com o terceiro = {soma}')
print(f'O terceiro elevado ao cubo = {potenciacao}')