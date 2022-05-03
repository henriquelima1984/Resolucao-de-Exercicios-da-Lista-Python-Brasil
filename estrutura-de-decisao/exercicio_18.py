# 18.Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

if 1 <= dia <= 31 and 1 <= mes <= 12:
    print(f'{dia} / {mes} / {ano}')
else:
    print('Data Inválida!')
