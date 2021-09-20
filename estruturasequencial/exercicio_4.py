"""
4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

>>> nota1 = float(input('Digite a nota1: '))
>>> nota2 = float(input('Digite a nota2: '))
>>> nota3 = float(input('Digite a nota3: '))
>>> nota4 = float(input('Digite a nota4: '))

>>> media = (nota1 + nota2 + nota3 + nota4) / 4

>>> print(f'Sua média foi {media}')

#Criamos uma lista e utilizamos ela dentro de um for(laço) para
#nos poupar do trabalho de criar uma variável para cada nota.
# E se fossem 300 notas?

>>> lista_de_notas = list(range(1, 5))
>>> soma_das_notas = 0
>>> media = 0

for _ in lista_de_notas:
    notas = float(input('Digite suas nota: '))
    soma_das_notas += notas
media = soma_das_notas / 4
print(f'Sua média foi {media}')

"""

lista_de_notas = []
soma = 0
media = 0

for n in range(4):
    notas = float(input('Nota ' + str(n+1) + ':\n'))
    lista_de_notas.append(notas)
    media += lista_de_notas[n] / 4
print(f'Sua média foi: {media}')