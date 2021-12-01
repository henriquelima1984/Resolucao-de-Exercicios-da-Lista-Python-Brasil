# 25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade
# da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
# conforme a média calculada.

qtd_de_pessoas = int(input('Informe a quantidade de pessoas: '))
soma_das_idades = 0
media_de_idade = 0

for n in range(0, qtd_de_pessoas):
    idade = float(input('Digite a ' + str(n + 1) + 'ª' + ' idade: '))
    soma_das_idades += idade
    media_de_idade = soma_das_idades / qtd_de_pessoas

print(f'Média de idade da turma é de {media_de_idade:.2f} anos')

if 0 <= media_de_idade <= 25:
    print('Portanto a turma é formada por jovens!')
elif 26 <= media_de_idade <= 60:
    print('Portanto a turma é formada por adultos!')
elif media_de_idade > 60:
    print('Portanto a turma é formada por jovens!')
