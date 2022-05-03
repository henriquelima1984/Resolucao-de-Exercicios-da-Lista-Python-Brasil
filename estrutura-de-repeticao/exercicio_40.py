# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 

# Foram obtidos os seguintes dados:

# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). 

# Deseja-se saber:

# a.Qual o maior e menor índice de acidentes de transito e a que cidade pertence?
# b.Qual a média de veículos nas cinco cidades juntas?

maior_indice_de_acidente = 0
menor_indice_de_acidente = 5_000_000_000

maior_codigo = 0
menor_codigo = 0

nome_cidade_1 = ''
nome_cidade_2 = ''

total_veiculos = 0
media_de_veiculos = 0


for n in range(1, 6):
    nome_da_cidade = input('Informe o nome da cidade: ')
    codigo_da_cidade = int(input('Informe o código da cidade: '))
    numero_de_veiculos_de_passeio = int(input('Informe o número de veículos: '))
    n_acidente_de_transito_com_vitimas = float(input('Informe o número de acidentes: '))
    print()

    total_veiculos += numero_de_veiculos_de_passeio

    if n_acidente_de_transito_com_vitimas > maior_indice_de_acidente:
        maior_indice_de_acidente = n_acidente_de_transito_com_vitimas
        maior_codigo = codigo_da_cidade
        nome_cidade_1 = nome_da_cidade
    
    if n_acidente_de_transito_com_vitimas < menor_indice_de_acidente:
        menor_indice_de_acidente = n_acidente_de_transito_com_vitimas
        menor_codigo = codigo_da_cidade
        nome_cidade_2 = nome_da_cidade
    
    media_de_veiculos = total_veiculos / n

print(f'''
Maior índice de acidente foi de {maior_indice_de_acidente:.0f} na cidade {maior_codigo} - {nome_cidade_1}
Menor índice de acidente foi de {menor_indice_de_acidente:.0f} na cidade {menor_codigo} - {nome_cidade_2}
Média de veículos => {media_de_veiculos:.0f}
''')
