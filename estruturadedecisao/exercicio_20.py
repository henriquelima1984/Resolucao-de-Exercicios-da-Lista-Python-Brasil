# 20.Faça um Programa para leitura de três notas parciais de um aluno.

# O programa deve calcular a média alcançada por aluno e apresentar:

# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

n1_parcial = float(input('Informe a nota: '))
n2_parcial = float(input('Informe a nota: '))
n3_parcial = float(input('Informe a nota: '))

media = (n1_parcial + n2_parcial + n3_parcial) / 3

if 7 <= media <= 9.99:
    print(f'Sua média foi {media:.2f} -> Aprovado!')
elif media < 7:
    print(f'Sua média foi {media:.2f} -> Reprovado!')
elif media == 10:
    print(f'Sua média foi {media:.2f} -> Aprovado com Distinção!')
