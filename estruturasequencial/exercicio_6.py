
# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

# Primeiro precisamos saber qual a fórmula matemática que calcula o círculo!

# >>> a = pi*r**2

# Agora podemos prosseguir com nosso programa!


raio = float(input('Digite o raio: '))

pi = 3.14
area_do_circulo = pi*raio**2

print(f'Área do círculo = {area_do_circulo}')