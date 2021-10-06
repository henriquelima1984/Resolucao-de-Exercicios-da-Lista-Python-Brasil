# 3.Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

#Utilizando expressões regulares restringimos o input apenas para aceitar letras!
#a função len --> mede o comprimento, fizemos com que letra não seja maior do que um caracter!

import re

letra = input('Digite uma letra: ').upper()

if not re.match("^[A-Z]*$", letra):
    print('ERROR: O caracter não é uma letra!')
elif len(letra) > 1:
    print('ERROR: só é permitido um carácter!')
elif letra == 'M':
    print('M - Masculino')
elif letra == 'F':
    print('F - Feminino')
else:
    print('Sexo Inválido')
