# 25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.As perguntas são:

# a."Telefonou para a vítima?"
# b."Esteve no local do crime?"
# c."Mora perto da vítima?"
# d."Devia para a vítima?"
# e."Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print()
print('FBI - Sistema de Criminalística')
print()

dicionario_de_perguntas = {
    'Pergunta 1': {
        'pergunta': 'Telefonou para a vítima?',
        'respostas': {'Opção_1': 'Sim', 'Opção_2': 'Não'},
        'opcao_1_do_interrogado': 'Sim',
        'opcao_2_do_interrogado': 'Não'
    },
    'Pergunta 2': {
        'pergunta': 'Esteve no local do crime?',
        'respostas': {'Opção_1': 'Sim', 'Opção_2': 'Não'},
        'opcao_1_do_interrogado': 'Sim',
        'opcao_2_do_interrogado': 'Não'
    },
    'Pergunta 3': {
        'pergunta': 'Mora perto da vítima?',
        'respostas': {'Opção_1': 'Sim', 'Opção_2': 'Não'},
        'opcao_1_do_interrogado': 'Sim',
        'opcao_2_do_interrogado': 'Não'
    },
    'Pergunta 4': {
        'pergunta': 'Devia dinheiro para a vítima?',
        'respostas': {'Opção_1': 'Sim', 'Opção_2': 'Não'},
        'opcao_1_do_interrogado': 'Sim',
        'opcao_2_do_interrogado': 'Não'
    },
    'Pergunta 5': {
        'pergunta': 'Já trabalhou com a vítima?',
        'respostas': {'Opção_1': 'Sim', 'Opção_2': 'Não'},
        'opcao_1_do_interrogado': 'Sim',
        'opcao_2_do_interrogado': 'Não'
    }
}

respostas_escolhidas_do_interrogado = 0
for key_1, value_1 in dicionario_de_perguntas.items():
    print(f'{key_1}: {value_1["pergunta"]}')

    print()
    for key_2, value_2 in value_1['respostas'].items():
        print(f'{key_2}: {value_2}')

    resposta_do_interrogado = input('Insira sua resposta: ')

    if resposta_do_interrogado == value_1['opcao_1_do_interrogado']:
        print('Analisando Resposta')
        respostas_escolhidas_do_interrogado += 1

    print()

qtd_de_perguntas = len(dicionario_de_perguntas)
resultado_do_interrogatorio = respostas_escolhidas_do_interrogado / qtd_de_perguntas

if resultado_do_interrogatorio == 0.2:
    print('Você está liberado!')

if resultado_do_interrogatorio == 0.4:
    print('Você é suspeito!')

if resultado_do_interrogatorio == 0.6 or resultado_do_interrogatorio == 0.8:
    print('Você é cúmplice!')

if resultado_do_interrogatorio == 1:
    print('Você é o assassino!')

print(f'Seu resultado -> {resultado_do_interrogatorio}')
