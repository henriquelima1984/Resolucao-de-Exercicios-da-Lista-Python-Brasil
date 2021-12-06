# 26.Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

print()
print('Bem-vindo ao sistema eleitoral Desordem e Regresso!')
print()
eleitores = int(input('Informe a quantidade de eleitores: '))
candidato_a = 0
candidato_b = 0
candidato_c = 0
qtd_votos = 0

while qtd_votos < eleitores:
    voto = int(input('''
Digite 1 para votar no candidato A
Digite 2 para votar no candidato B
Digite 3 para votar no candidato C
Vote: '''))

    if voto == 1:
        candidato_a += 1
    elif voto == 2:
        candidato_b += 1
    elif voto == 3:
        candidato_c += 1
    qtd_votos += 1

print(f'''Candidato A teve {candidato_a} voto(s).
Candidato B teve {candidato_b} voto(s)
Candidato C teve {candidato_c} voto(s)''')
