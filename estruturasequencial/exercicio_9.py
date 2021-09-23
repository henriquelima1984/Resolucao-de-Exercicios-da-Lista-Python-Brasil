# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
# C = 5 * ((F-32) / 9). Equação para realizar a conversão de temperatura.
# Para poupar ter que transformar Celsius em Fahrenheit também em exercícios separados
# Decidi criar um while e fazer um menu de opções para você escolher qual operação deseja fazer

option = 0
while option != 3:
    print('''    [1] - Converter de (°F) para (°C)
    [2] - Converter de (°C) para (°F)
    [3] - Exit
    ''')
    option = int(input('Escolha uma opção:'))
    if option == 1:
        f = float(input('Digite a temperatura em (°F): '))
        celsius = 5 * ((f - 32) / 9)
        print(f'Temperatura em (°C) = {celsius} ')
    elif option == 2:
        c = float(input('Digite a temperaturam em (°C): '))
        fahrenheit = (c * 9 / 5) + 32
        print(f'Temperatura em (°F) = {fahrenheit}')
    elif option == 3:
        print('Programa encerrado!')
    else:
        print('Opção inválida tente novamente!')
