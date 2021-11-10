# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    usuario = input('user: ')
    senha = input('Password: ')
    if usuario != senha:
        print('Autenticação válida!')
        break
    else:
        print('Nome de usuário não pode ser igual a senha!')
        continue
