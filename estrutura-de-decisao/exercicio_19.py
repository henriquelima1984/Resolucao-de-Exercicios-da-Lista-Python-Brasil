# 19.Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades
# do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros.
# Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = int(input('Digite um número: '))

centena = numero // 100
dezena = numero // 10 % 10
unidade = numero % 10

if numero >= 1000:
    print('ERROR: número não pode ser maior ou igual à 1000!')

elif centena > 1 and dezena > 1 and unidade > 1:
    print(f'{numero} = {centena} centenas, {dezena} dezenas e {unidade} unidades')

elif centena == 1 and dezena == 1 and unidade == 1:
    print(f'{numero} = {centena} centena, {dezena} dezena e {unidade} unidade')

elif centena > 1 and dezena == 1 and unidade == 1:
    print(f'{numero} = {centena} centenas, {dezena} dezena e {unidade} unidade')

elif centena == 1 and dezena == 0 and unidade == 0:
    print(f'{numero} = {centena} centena')

elif centena > 1 and dezena == 0 and unidade == 0:
    print(f'{numero} = {centena} centenas')

elif centena == 1 and dezena > 1 and unidade > 1:
    print(f'{numero} = {centena} centena, {dezena} dezenas e {unidade} unidades')

elif centena == 1 and dezena == 1 and unidade > 1:
    print(f'{numero} = {centena} centena, {dezena} dezena e {unidade} unidades')

elif centena == 1 and dezena > 1 and unidade == 1:
    print(f'{numero} = {centena} centena, {dezena} dezenas e {unidade} unidade')

elif centena > 1 and dezena > 1 and unidade == 1:
    print(f'{numero} = {centena} centenas, {dezena} dezenas e {unidade} unidade')

elif centena > 1 and dezena == 1 and unidade > 1:
    print(f'{numero} = {centena} centenas, {dezena} dezena e {unidade} unidades')

elif centena == 1 and dezena == 0 and unidade == 1:
    print(f'{numero} = {centena} centena, {unidade} unidade')

elif centena > 1 and dezena == 0 and unidade > 1:
    print(f'{numero} = {centena} centenas, {unidade} unidades')

elif centena == 1 and dezena == 0 and unidade > 1:
    print(f'{numero} = {centena} centena, {unidade} unidades')

elif centena > 1 and dezena == 0 and unidade == 1:
    print(f'{numero} = {centena} centenas, {unidade} unidade')

elif centena > 1 and dezena == 1 and unidade == 0:
    print(f'{numero} = {centena} centenas e {dezena} dezena')

elif centena > 1 and dezena > 1 and unidade == 0:
    print(f'{numero} = {centena} centenas e {dezena} dezenas')

elif centena == 1 and dezena > 1 and unidade == 0:
    print(f'{numero} = {centena} centena e {dezena} dezenas')

elif centena == 1 and dezena == 1 and unidade == 0:
    print(f'{numero} = {centena} centena e {dezena} dezena')

elif centena == 0 and dezena == 1 and unidade == 1:
    print(f'{numero} = {dezena} dezena e {unidade} unidade')

elif centena == 0 and dezena == 1 and unidade > 1:
    print(f'{numero} = {dezena} dezena e {unidade} unidades')

elif centena == 0 and dezena > 1 and unidade == 1:
    print(f'{numero} = {dezena} dezenas e {unidade} unidade')

elif centena == 0 and dezena > 1 and unidade > 1:
    print(f'{numero} = {dezena} dezenas e {unidade} unidades')

elif centena == 0 and dezena == 1 and unidade == 0:
    print(f'{numero} = {dezena} dezena')

elif centena == 0 and dezena > 1 and unidade == 0:
    print(f'{numero} = {dezena} dezenas')

elif centena == 0 and dezena == 0 and unidade == 1:
    print(f'{numero} = {unidade} unidade')

elif centena == 0 and dezena == 0 and unidade > 1:
    print(f'{numero} = {unidade} unidades')
