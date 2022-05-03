# 5.Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
# números IMPARES no vetor impar. Imprima os três vetores.

lista_numeros = []
lista_impares = []
lista_pares = []

for _ in range(21):
    numero = int(input('Digite um número: '))

    lista_numeros.append(numero)

    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(lista_numeros)
print(lista_pares)
print(lista_impares)
