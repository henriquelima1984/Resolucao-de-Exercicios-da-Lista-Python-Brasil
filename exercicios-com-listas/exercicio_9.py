# 9.Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos
# do vetor.

vetorA = []
soma_dos_quadrados = 0

for _ in range(3):
    numero = int(input('Informe um número: '))
    vetorA.append(numero ** 2)
    soma_dos_quadrados = sum(vetorA)

print()
print(f'''vetorA²: {vetorA}
Soma dos quadrados dos elementos: {soma_dos_quadrados}''')
