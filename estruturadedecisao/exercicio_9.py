# 9.Faça um Programa que leia três números e mostre-os em ordem decrescente.

"""
Utilizando lista -->

lista_numeros = []
ordem_decrescente = 0

for n in range(3):
    numero = float(input('Digite o número ' + str(n + 1) + ':' + '\n'))
    lista_numeros.append(numero)
    lista_numeros.sort(reverse=True)
print(lista_numeros)

"""
# Utilizando estrutura de decisão

number_1 = float(input('Digite o primeiro número: '))
number_2 = float(input('Digite o segundo  número: '))
number_3 = float(input('Digite o terceiro número: '))

if number_1 < number_2 < number_3:
    print(f'em ordem decrescente:{number_3},{number_2},{number_1}')
elif number_1 < number_3 < number_2:
    print(f'em ordem decrescente:{number_2},{number_3},{number_1}')
elif number_2 < number_3 < number_1:
    print(f'em ordem decrescente:{number_1},{number_3},{number_2}')
elif number_3 < number_2 < number_1:
    print(f'em ordem decresente:{number_1},{number_2}, {number_3}')
elif number_2 < number_1 < number_3:
    print(f'em ordem decrescente:{number_3},{number_1},{number_2}')
elif number_3 < number_1 < number_2:
    print(f'em ordem decrescente:{number_2},{number_1},{number_3}')
