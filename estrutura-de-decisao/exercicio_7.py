# 7.Faça um Programa que leia três números e mostre o maior e o menor deles.
# Esse exercício é muito parecido com o anterior!
# Essa é a minha solução sem utilizar estrutura de decisão!
# ATENÇÃO : sugiro que você tente resolver utilizando if/elif/else,
# pois assim você fixa o conteúdo!

numeros = []
max_value = 0
min_value = 0

for _ in range(3):
    valor = float(input('Digite os valores: '))
    numeros.append(valor)
    max_value = max(numeros)
    min_value = min(numeros)
print(f'''O maior valor é: {max_value}
O menor valor é: {min_value}''')
