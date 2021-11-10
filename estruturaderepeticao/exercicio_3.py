# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

print()
print('Preencha o formulário')
print()

nome = (input('Informe seu nome: '))
while len(nome) <= 3:
    nome = (input('Informe seu nome: '))

idade = int(input('Informe sua idade: '))
while idade > 150 or idade < 0:
    idade = int(input('Informe sua idade: '))

salario = float(input('Informe aqui seu salário: '))
while salario < 1:
    salario = float(input('Informe aqui seu salário: '))

sexo = (input('Informe seu sexo: ')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = (input('Informe seu sexo: ')).upper()

estado_civil = (input('Informe seu estado civil: ')).upper()
while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
    estado_civil = (input('Informe seu estado civil: ')).upper()

print()
print('Cadastro realizado com sucesso')
print()

print(f'''Nome: {nome}
Idade: {idade} anos
Salário: R$ {salario:.2f}
Sexo: {sexo} 
Estado Civil: {estado_civil}''')
