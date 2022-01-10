# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
# Um número primo é aquele que é divisível apenas por um e por ele mesmo.
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

print()
print('Números Primos')
print()

n = int(input('Informe um número: '))
mult = 0

for count in range(2, n):
    if n % count == 0:
        print(f'Múltiplo de {count}')
        mult += 1

if mult == 0:
    print('É primo')
else:
    print(f'Tem {mult} múltiplos ácima de 2 e abaixo de {n}')
