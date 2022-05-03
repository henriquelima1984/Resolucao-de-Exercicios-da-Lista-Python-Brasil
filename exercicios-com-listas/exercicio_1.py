# 1.Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista_de_numeros = []

for _ in range(1, 6):
    numero = int(input('Informe um número: '))
    lista_de_numeros.append(numero)
print(lista_de_numeros)
