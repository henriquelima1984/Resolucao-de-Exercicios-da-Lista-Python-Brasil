# 10.Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Em qual turno você estuda? ')

if turno == "M-Matutino":
    print("Bom Dia")
elif turno == "V-Vespertino":
    print("Boa Tarde")
elif turno == "N-Noturno":
    print("Boa Noite")
else:
    print("Opção Inválida")
