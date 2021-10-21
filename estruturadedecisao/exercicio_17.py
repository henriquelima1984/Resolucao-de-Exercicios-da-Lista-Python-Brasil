# 17.Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe
# se este ano é ou não bissexto.

# Bissexto - Um ano é bissexto se ele for divisível por 400
# ou se ele for divisível por 4 e não por 100.
# Bissexto:  1980, 1984, 1988, 1992, 1996 e 2000.
# 1900 não foi bissexto, mas 1600 foi

ano = int(input('Informe um ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto! ')
else:
    print('O ano não é bissexto! ')
