# 4.Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista_caracteres = []
lista_vogais = ['a', 'e', 'i', 'o', 'u']
qtd_vogal = 0
consoantes = 0

for _ in range(10):
    caracter = input('Informe um caracter: ')
    lista_caracteres.append(caracter)

    if caracter in lista_vogais:
        qtd_vogal += 1
    else:
        consoantes = len(lista_caracteres) - qtd_vogal

print(f'''Todos os caracteres : {lista_caracteres} 
Quantidade de vogais : {qtd_vogal}
Quantidade de consoantes : {consoantes}''')
