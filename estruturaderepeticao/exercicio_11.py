# 11.Altere o programa anterior para mostrar no final a soma dos números.

print()
print('Algoritmo para filtrar números inteiros em um intervalo qualquer.')
print()

inicio = int(input('Digite o valor de início: '))
fim = int(input('Digite o valor final: '))
soma = 0

for n in range(inicio + 1, fim, 1):
    print(n)
    soma += n
print(f'A soma dos números no intervalo de {inicio} a {fim} é igual a {soma}')
