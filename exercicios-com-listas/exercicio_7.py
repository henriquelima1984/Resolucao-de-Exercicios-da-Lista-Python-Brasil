# 7.Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

from functools import reduce
from operator import mul

lista_numeros = []
soma = 0
multiplicacao = 0

for _ in range(5):
    numero = int(input('Informe um número inteiro: '))
    lista_numeros.append(numero)
    soma = sum(lista_numeros)
    multiplicacao = reduce(mul, lista_numeros, 1)

print()
print(f'''Vetor: {lista_numeros}
Resultado
Soma: {soma}
Produto: {multiplicacao}''')
