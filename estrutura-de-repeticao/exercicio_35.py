# 35.Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes
# entre 1 e um número inteiro informado pelo usuário.

# Se o resto da divisão for zero o número não é primo.
# Se nenhum resto for zero o número é primo.

print()
print('Lista de Números Primos')
print()

# verificando se o número é primo


def primo(n):
    for val in range(2, n):
        if n % val == 0:
            return False
    return True


def lista_de_primos():
    n = int(input('\nMostrar sequência até: '))
    for val in range(2, n + 1):
        if primo(val):
            print(f'{val}', end=' ')


while True:
    lista_de_primos()
