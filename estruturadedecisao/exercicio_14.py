# 14.Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

media = (n1 + n2) / 2
print(f'Média = {media}')

if 9 <= media <= 10:
    print('Conceito A')
elif 7.5 <= media < 9:
    print('Conceito B')
elif 6 <= media <= 7.5:
    print('Conceito C')
elif 4 <= media <= 6:
    print('Conceito D')
else:
    print('Conceito E')
