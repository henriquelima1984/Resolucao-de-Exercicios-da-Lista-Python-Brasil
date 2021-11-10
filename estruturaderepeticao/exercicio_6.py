# 6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

print()
numeros = {1: ' - Números na vertical', 2: ' - Números da horizontal', 3: ' - Exit'}

for key, value in numeros.items():
    print(key, value)
option = int(input('Make your choice: '))

if option == 1:
    for x in range(1, 21):
        print(x)

if option == 2:
    for x in range(1, 21):
        print(x, end=' ')

if option == 3:
    print('Encerrado!')
