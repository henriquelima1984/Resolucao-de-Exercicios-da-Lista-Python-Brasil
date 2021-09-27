#14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
#deve pagar uma multa de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
#Imprima os dados do programa com as mensagens adequadas.

peso_dos_peixes = float(input('Informe o peso dos peixes: '))
peso_limite = 50
excesso = peso_dos_peixes - peso_limite
multa_por_excesso = excesso * 4

if peso_dos_peixes <= peso_limite:
    print('Você está dentro do regulamento, não pagará multa!')
elif peso_dos_peixes > peso_limite:
    print(f'Ultrapassou 50 kg,você pagará uma multa por kilo adicional no valor de {multa_por_excesso} R$')
