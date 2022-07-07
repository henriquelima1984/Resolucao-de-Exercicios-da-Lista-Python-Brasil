# 6.Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo,
# o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo
# menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação
# A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões
# terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário
# repita esse cálculo para novos valores de entrada todas as vezes que desejar.


def converter_formato_horas(horario):
    if 13 <= horario <= 23:
        return f'Horário no formato 12 horas -> {horario - 12:.2f} p.m'

    if horario == 0:
        return f'Horário no formato 12 horas -> {horario + 12} a.m'

    if horario == 12:
        return f'Horário no formato 12 horas -> {horario} p.m'

    if 0 <= horario <= 11:
        return f'Horário no formato 12 horas -> {horario} a.m'


while True:
    print()
    converter = converter_formato_horas(float(input('Conversão horário formato 24 horas -> 12 horas: ')))
    print(converter)

    exit = input('Deseja sair? ')

    if exit == 's':
        break
    else:
        continue
