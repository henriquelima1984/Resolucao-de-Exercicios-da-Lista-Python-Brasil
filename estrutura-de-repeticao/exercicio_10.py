# 10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido
# por eles.

print()
print('Algoritmo para filtrar números inteiros em um intervalo qualquer.')
print()

inicio = int(input('Digite o valor de início: '))
fim = int(input('Digite o valor final: '))

for n in range(inicio + 1, fim, 1):
    print(n)
