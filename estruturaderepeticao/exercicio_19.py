# 19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

print()
resp = 'S'
quantidade = maior = menor = 0
while resp in 'Ss':
    numero = int(input('Digite um número: '))

    quantidade += 1

    if numero < 0 or numero > 1000:
        quantidade += 1
        print('Error: Apenas números entre 0 e 1000 serão considerados válidos!')
        continue

    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        resp = input('Quer continuar? [S/N]: ').upper().strip()[0]

print(f'''O menor valor é {menor}
O maior valor é {maior}''')
