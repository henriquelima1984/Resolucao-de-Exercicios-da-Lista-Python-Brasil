# 6.Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima
# o número de alunos com média maior ou igual a 7.0.

lista_alunos = []
lista_medias = []
aprovados = 0

for aluno in range(10):
    alunos = input('Nome do aluno: ')
    lista_alunos.append(alunos)
    notas = 0
    for nota in range(4):
        notas += float(input('Digite a ' + str(nota + 1) + 'ª' + ' nota: '))
    lista_medias.append(notas/4)

    if lista_medias[aluno] >= 7:
        aprovados += 1

print()
print(f'''{lista_alunos}
{lista_medias:.2f}
Alunos aprovados: {aprovados}''')
