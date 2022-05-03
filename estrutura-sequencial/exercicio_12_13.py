# 12 e 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
# Utilizei :.2f para diminuir casas decimais

menu_peso = {1: 'Calcule seu peso (Homem)', 2: 'Calcule seu peso (Mulher)', 3: 'Exit'}

while True:
    for key, value in menu_peso.items():
        print(key, value)
    option = int(input('Make your choice: '))
    if option == 1:
        h_homem = float(input('Informe sua altura: '))
        peso_homem = (72.7*h_homem) - 58
        print(f'Você está pesando: {peso_homem:.2f} kg')
    elif option == 2:
        h_mulher = float(input('Informe sua altura: '))
        peso_mulher = (62.1*h_mulher) - 44.7
        print(f'Você está pesando: {peso_mulher:.2f} kg')
    elif option == 3:
        print('Programa encerrado!')
        break
    else:
        print('Invalid choice, try again!')
