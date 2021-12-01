# 24.Faça um programa que calcule o mostre a média aritmética de N notas.

qtd_notas = int(input('Digite a quantidade de notas: '))
soma = 0
media = 0

for c in range(0, qtd_notas):
    notas = float(input('Digite sua ' + str(c + 1) + 'ª' + ' nota: '))
    soma += notas
    media = soma/qtd_notas
print(f'Sua média foi {media}')
