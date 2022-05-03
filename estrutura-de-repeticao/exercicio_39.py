# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

num_maior_aluno = 0
num_menor_aluno = 0

aluno_mais_alto = 0
aluno_mais_baixo = 2.72

for _ in range(1, 3):
    numero = int(input('Informe seu número: '))
    altura = int(input('Informe sua altura: '))

    if altura > aluno_mais_alto:
        aluno_mais_alto = altura
        num_maior_aluno = numero
    
    if altura < aluno_mais_baixo:
        aluno_mais_baixo = altura
        num_menor_aluno = numero

print(f'''Aluno mais alto : {num_maior_aluno} Altura : {aluno_mais_alto:.2f} m
Aluno mais baixo : {num_menor_aluno} Altura : {aluno_mais_baixo:.2f} m''')
