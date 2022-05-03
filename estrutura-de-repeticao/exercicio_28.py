# 28.Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio
# gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

print()
qtd_de_cds = int(input('Quantidade de Cds: '))
valor_total = 0
valor_medio_gasto = 0

for cd in range(qtd_de_cds):
    valor_gasto_por_cd = float(input('Valor gasto no CD ' + str(cd + 1) + ': '))

    valor_total += valor_gasto_por_cd
    valor_medio_gasto = valor_total / qtd_de_cds
print(f'''Valor total gasto na coleção foi de {valor_total:.2f} reais
Valor médio gasto na sua coleção foi de {valor_medio_gasto:.2f} reais''')
