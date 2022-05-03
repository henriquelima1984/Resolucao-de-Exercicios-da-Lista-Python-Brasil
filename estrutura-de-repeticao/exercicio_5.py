# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

print()
populacao_menu = {'1': ' - Comparar taxa de crescimento entre populações', '2': ' - Exit'}

while True:
    for key, value in populacao_menu.items():
        print(key, value)
    option = input('Escolha uma opção: ')

    if option == '1':
        populacao_a = int(input('População de A: '))
        populacao_b = int(input('População de B: '))
        taxa_de_crescimento_de_a = float(input('Taxa de crescimento de A: '))
        taxa_de_crescimento_de_b = float(input('Taxa de crescimento de B: '))
        anos = 0

        while populacao_a < populacao_b:
            print(f'{anos} ano(s)')
            print(f'População A -> {populacao_a} habitantes')
            print(f'População B -> {populacao_b} habitantes')

            populacao_a = round((populacao_a * taxa_de_crescimento_de_a))
            populacao_b = round((populacao_b * taxa_de_crescimento_de_b))
            anos += 1

        print(f'{anos} ano(s)')
        print(f'População A -> {populacao_a} habitantes')
        print(f'População B -> {populacao_b} habitantes')

    if option == '2':
        break
