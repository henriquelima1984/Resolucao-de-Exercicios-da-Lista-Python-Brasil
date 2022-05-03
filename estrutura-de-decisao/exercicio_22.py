# 22.Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).
# Se o valor retornado da divisão for diferente de zero, o número é ímpar!

numero1 = float(input('Informe um número: '))
numero2 = float(input('Informe um número: '))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print(f'{numero1} -> Par')
    print(f'{numero2} -> Par')

if numero1 % 2 != 0 and numero2 % 2 != 0:
    print(f'{numero1} -> Ímpar')
    print(f'{numero2} -> Ímpar')

if numero1 % 2 == 0 and numero2 % 2 != 0:
    print(f'{numero1} -> Par')
    print(f'{numero2} -> Ímpar')

if numero1 % 2 != 0 and numero2 % 2 == 0:
    print(f'{numero1} -> Ímpar')
    print(f'{numero2} -> Par')
