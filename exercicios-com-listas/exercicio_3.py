# 3.Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista_notas = []
soma = 0
media = 0

for n in range(4):
    nota = float(input('Informe a ' + str(n + 1) + 'ª' + ' nota: '''))
    lista_notas.append(nota)
    soma = sum(lista_notas)
    media = soma / len(lista_notas)
print(f'''Notas : {lista_notas} 
Média : {media:.2f}''')
