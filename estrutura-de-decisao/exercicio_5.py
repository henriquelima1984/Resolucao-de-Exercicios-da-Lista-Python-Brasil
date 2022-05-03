# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
# aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota_parcial_1 = float(input('Nota parcial 1:' + '\n'))
nota_parcial_2 = float(input('Nota parcial 2:' + '\n'))
media = (nota_parcial_1 + nota_parcial_2) / 2

if media == 10:
    print("Aprovado com distinção!")
elif media >= 7:
    print("Aprovado!")
elif media < 7:
    print("Reprovado!")
