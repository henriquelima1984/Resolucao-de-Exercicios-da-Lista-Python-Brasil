# 15.Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
# triangulo, indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado_a = float(input("Digite o primeiro lado do triângulo: "))
lado_b = float(input("Digite o segundo  lado do triângulo: "))
lado_c = float(input("Digite o terceiro lado do triângulo: "))

soma_ab = lado_a + lado_b
soma_ac = lado_a + lado_c
soma_bc = lado_b + lado_c

if soma_ab == lado_c:
    print("Impossível formar um triângulo")
elif soma_ac == lado_b:
    print("Impossível formar um triângulo")
elif soma_bc == lado_a:
    print("Impossível formar um triângulo")
elif lado_a == lado_b == lado_c:
    print("Equilátero")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("Isósceles")
elif lado_a != lado_b != lado_c:
    print("Escaleno")
