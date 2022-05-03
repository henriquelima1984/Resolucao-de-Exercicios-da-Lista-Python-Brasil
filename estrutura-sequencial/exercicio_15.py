# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

#Obs.: Salário Bruto - Descontos = Salário Líquido.

ganho_por_hora = float(input('Informe o valor da hora trabalhada: '))
qtd_horas_trabalhadas_no_mes = float(input('Informe as horas trabalhadas no mês: '))

salario_bruto = ganho_por_hora * qtd_horas_trabalhadas_no_mes
desconto_inss = 8/100 * salario_bruto
desconto_sindicato = 5/100 * salario_bruto
desconto_ir = 11/100 * salario_bruto
salario_liquido = salario_bruto - desconto_inss - desconto_sindicato - desconto_ir

print(f'Salário Bruto -> {salario_bruto} R$')
print(f'Desconto INSS -> {desconto_inss} R$')
print(f'Desconto Sindicato -> {desconto_sindicato} R$')
print(f'Desconto I.R -> {desconto_ir} R$')
print(f'Salário Líquido -> {salario_liquido:.2f} R$')
