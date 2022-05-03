# 23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.

numero = float(input("Digite um número: "))

if numero * 10 % 10 == 0:
    print("Inteiro")
else:
    print("Decimal")
