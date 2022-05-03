# 1.Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    try:
        nota = int(input('Informe a nota: '))
    except ValueError:
        print('Deve ser fornecido um valor inteiro!')
    else:
        if 0 <= nota <= 10:
            print(f'Nota do aluno foi {nota}')
            break
        else:
            print('Valor Inválido!')
