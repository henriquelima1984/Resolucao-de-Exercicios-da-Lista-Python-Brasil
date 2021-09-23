
# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

ganho_por_hora = float(input('Digite o valor da hora trabalhada: '))
horas_trabalhadas_no_mes = int(input('Digite o número de horas trabalhadas no mês: '))

salario_no_mes = ganho_por_hora * horas_trabalhadas_no_mes
print(f'O valor do seu salário é: {salario_no_mes} R$')
