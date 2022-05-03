# 21.Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.


print()
print('Crivo de Eratóstenes')
print()

num = int(input('Informe um número: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print()
print(f'\n\033[mO número {num} foi divisível por {total} número(s)')
print()
if total == 2:
    print('Portanto ele é primo.')
else:
    print('Portanto ele não é primo.')
