# 10.Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores
# deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetorNome = []
vetorIdade = []

for _ in range(3):
    nome = input('Informe seu nome: ')
    vetorNome.append(nome)

for _ in range(3):
    idade = input('Informe sua idade: ')
    vetorIdade.append(idade)

vetordados = vetorNome + vetorIdade

vetordados[::2] = vetorNome  # significa que vetorNome vai ocupar a primeira posição [0] - Henrique
vetordados[1::2] = vetorIdade  # 1:: significa que a idade vai ocupar a posição dois [1] - 25

print(vetordados)
