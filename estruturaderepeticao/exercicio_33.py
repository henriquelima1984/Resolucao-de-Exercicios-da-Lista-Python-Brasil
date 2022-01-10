# 33.O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto
# indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das
# temperaturas.

print()
print('Medidor de temperatura')
print()

temperatura = int(input('Informe o número de temperaturas a serem lidas: '))
print()

maior_temperatura = menor_temperatura = celsius = media_das_temperaturas = 0

for _ in range(temperatura):
    c = float(input('Informe a temperatura em °C: '))

    media_das_temperaturas += c / temperatura

    celsius += 1

    if celsius == 1:
        maior_temperatura = menor_temperatura = c
    else:
        if c > maior_temperatura:
            maior_temperatura = c

        if c < menor_temperatura:
            menor_temperatura = c

print()
print(f'''A maior temperatura registrada foi de {maior_temperatura:.2f}°C
A menor temperatura registrada foi de {menor_temperatura:.2f}°C
A temperatura média é de {media_das_temperaturas:.2f}°C''')
