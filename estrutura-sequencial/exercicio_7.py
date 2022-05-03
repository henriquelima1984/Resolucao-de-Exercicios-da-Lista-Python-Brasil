
# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

# Primeiro precisamos saber qual a fórmula matemática que calcula á área do quadrado!

# >>> area_quadrado = l**2

# 2**3 --> dois asteriscos representa potência no python

lado_do_quadrado = int(input('Digite o lado do quadrado: '))

area_do_quadrado = (lado_do_quadrado**2)
dobro_da_area_do_quadrado = area_do_quadrado * 2

print(f"""Área do quadrado = {area_do_quadrado}  
Dobro da área do quadrado = {dobro_da_area_do_quadrado} """ )