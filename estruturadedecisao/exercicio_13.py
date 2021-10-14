# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dias_da_semana = int(input('Digite um número: '))

if dias_da_semana == 1:
    print('Domingo')
elif dias_da_semana == 2:
    print('Segunda')
elif dias_da_semana == 3:
    print('Terça')
elif dias_da_semana == 4:
    print('Quarta')
elif dias_da_semana == 5:
    print('Quinta')
elif dias_da_semana == 6:
    print('Sexta')
elif dias_da_semana == 7:
    print('Sábado')
else:
    print('Operação inválida, a semana só tem 7 dias!')
