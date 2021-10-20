# 16.Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c = 0.
# O programa deverá pedir os valores de a, b e c e fazer as consistências,informando ao usuário nas seguintes situações:

# a.Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve
# pedir os demais valores, sendo encerrado;
# b.Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# c.Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# d.Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))

calc_delta = b**2 - 4 * a * c

if a == 0:
    print('A equação não é do 2° Grau.')
elif calc_delta == 0:
    print('A equação possui apenas uma raiz real.')
elif calc_delta > 0:
    raiz_de_delta = math.sqrt(calc_delta)
    print('A equação possui duas raízes reais.')
    x_linha = (-b + raiz_de_delta) / 2 * a
    x_linha_linha = (-b - raiz_de_delta) / 2 * a
elif calc_delta < 0:
    print('A equação não possui raízes reais.')
