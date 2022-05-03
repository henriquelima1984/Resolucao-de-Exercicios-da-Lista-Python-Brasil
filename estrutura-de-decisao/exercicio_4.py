# 4.Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

import re

dicionario_de_vogais = {1: 'A', 2: 'E', 3: 'I', 4: 'O', 5: 'U'}

dicionario_de_consoantes = {1: 'B', 2: 'C', 3: 'D', 4: 'F', 5: 'G', 6: 'H', 7: 'J', 8: 'K', 9: 'L', 10: 'M', 11: 'N',
12: 'P', 13: 'Q', 14: 'R', 15: 'S', 16: 'T', 17: 'V', 18: 'X', 19: 'Y', 20: 'W', 21: 'Z'}

letra = input('Digite uma letra: ').upper()

for vogal in dicionario_de_vogais.values():
    if letra == vogal:
        print('É uma vogal!')
for consoante in dicionario_de_consoantes.values():
    if letra == consoante:
        print('É uma consoante!')

if not re.match("^[A-Z]*$", letra):
    print('ERROR: o caracter não é uma letra!')
elif len(letra) > 1:
    print('ERROR: só é permitido um caracter!')
