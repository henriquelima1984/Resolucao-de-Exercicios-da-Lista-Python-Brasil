# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
media = 0

for n in range(5):
    numeros = float(input('Informe o ' + str(n + 1) + 'º' + ' número: ' + '\n'))
    soma += numeros
    media = soma / 5
print(f'''Soma dos números = {soma}
Média = {media}''')
