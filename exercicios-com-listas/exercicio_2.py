# 2.Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista_numeros_reais = []
ordem_inversa = 0

for _ in range(1, 5):
    numero = int(input('Informe um número: '))
    lista_numeros_reais.append(numero)
print(list(reversed(lista_numeros_reais)))
