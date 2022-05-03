# 8.Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.


vetor_idade = []
vetor_altura = []

for _ in range(5):
    idade = int(input('Informe sua idade: '))
    altura = float(input('Informe sua altura: '))

    vetor_idade.append(idade)
    vetor_altura.append(altura)

print()
print('Ordem Inversa: Idade')
print(list(reversed(vetor_idade)))
print('Ordem Inversa: Altura')
print(list(reversed(vetor_altura)))
