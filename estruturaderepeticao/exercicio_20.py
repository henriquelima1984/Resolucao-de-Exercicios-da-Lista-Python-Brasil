# 20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando
# o fatorial a números inteiros positivos e menores que 16.

resp = ''
n = 0
while resp != 'N':
    n = int(input('Digite um número para calcular o fatorial: '))
    fat = 1
    if 1 <= n <= 16:
        for i in range(n):
            i += 1
            fat *= i
        print(f'{n}! = {fat}')
    else:
        print('Error: Só é permitido números inteiros positivos e menores que 16.')

    resp = input('Deseja continuar? [Y/N]: ').upper().strip()[0]

    if resp == 'Y':
        continue
    else:
        break
