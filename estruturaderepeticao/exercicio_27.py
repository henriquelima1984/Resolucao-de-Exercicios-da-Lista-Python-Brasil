# 27.Faça um programa que calcule o número médio de alunos por turma. Para isto,
# peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

from math import floor

print()
print('Estatística de alunos por turma')
print()

qtd_de_turmas = int(input('Quantidade de turmas: '))
soma = 0
media = 0

for turma in range(qtd_de_turmas):
    qtd_de_alunos = int(input('Quantidade de alunos na turma ' + str(turma + 1) + ': '))

    if qtd_de_alunos > 40:
        print('Capacidade máxima de 40 alunos por sala.')
        continue

    soma += qtd_de_alunos
    media = soma / qtd_de_turmas
print(f'Número médio é de {floor(media)} alunos por turma.')
