# 24.Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

menu = {1: '- Par ou Ímpar', 2: '- Positivo ou Negativo', 3: '- Inteiro ou Decimal', 4: 'Exit'}

while True:
    n1 = float(input('Informe n1: '))
    n2 = float(input('Informe n2: '))
    print()
    for key, value in menu.items():
        print(key, value)
    print()
    option = int(input('Qual operação deseja realizar? '))
    print()
    if option == 1:
        if n1 % 2 == 0 and n2 % 2 == 0:
            print(f'{n1} -> Par')
            print(f'{n2} -> Par')

        if n1 % 2 != 0 and n2 % 2 != 0:
            print(f'{n1}-> Ímpar')
            print(f'{n2} -> Ímpar')

        if n1 % 2 == 0 and n2 % 2 != 0:
            print(f'{n1} -> Par')
            print(f'{n2} -> Ímpar')

        if n1 % 2 != 0 and n2 % 2 == 0:
            print(f'{n1} -> Ímpar')
            print(f'{n2} -> Par')

    if option == 2:
        if n1 < 0 and n2 < 0:
            print(f'{n1} -> Negativo')
            print(f'{n2} -> Negativo')
            print()

        if n1 > 0 and n2 > 0:
            print(f'{n1} -> Positivo')
            print(f'{n2} -> Positivo')
            print()

        if n1 < 0 < n2:
            print(f'{n1} -> Negativo')
            print(f' {n2} -> Positivo')
            print()

        if n1 > 0 > n2:
            print(f' {n1} -> Positivo')
            print(f'{n2} -> Negativo')
            print()

    if option == 3:
        if n1 * 10 % 10 == 0 and n2 * 10 % 10 == 0:
            print(f'{n1} -> Inteiro')
            print(f'{n2} -> Inteiro')
            print()

        if n1 * 10 % 10 != 0 and n2 * 10 % 10 != 0:
            print(f'{n1} -> Decimal')
            print(f'{n2} -> Decimal')
            print()

        if n1 * 10 % 10 == 0 and n2 * 10 % 10 != 0:
            print(f'{n1} -> Inteiro')
            print(f'{n2} -> Decimal')
            print()

        if n1 * 10 % 10 != 0 and n2 * 10 % 10 == 0:
            print(f'{n1} -> Decimal')
            print(f'{n2} -> Inteiro')
            print()

    if option == 4:
        print('Programa encerrado!')
        break
    else:
        print('')
