# 14.Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade
# de números impares.

impar = 0
par = 0
print()
for count in range(4):
    numero = int(input('Digite o ' + str(count + 1) + '° ' + 'número: '))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
print()
print(f'''Quantidade de números pares = {par}  
Quantidade de números ímpares = {impar}''')
