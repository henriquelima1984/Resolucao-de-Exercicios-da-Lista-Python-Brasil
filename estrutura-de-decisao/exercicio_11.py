# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
# e lhe contrataram para desenvolver o programa que calculará os reajustes.

# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%

# Após o aumento ser realizado, informe na tela:

# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Digite aqui seu salário:'))

reajuste_salarial_1 = (0.20 * salario) + salario
reajuste_salarial_2 = (0.15 * salario) + salario
reajuste_salarial_3 = (0.10 * salario) + salario
reajuste_salarial_4 = (0.05 * salario) + salario

percentual_de_aumento_1 = reajuste_salarial_1 / salario
percentual_de_aumento_2 = reajuste_salarial_2 / salario
percentual_de_aumento_3 = reajuste_salarial_3 / salario
percentual_de_aumento_4 = reajuste_salarial_4 / salario

valor_do_aumento_1 = reajuste_salarial_1 - salario
valor_do_aumento_2 = reajuste_salarial_2 - salario
valor_do_aumento_3 = reajuste_salarial_3 - salario
valor_do_aumento_4 = reajuste_salarial_4 - salario

if salario <= 280:
    print(f'Seu salário é: {salario} R$')
    print(f'O percentual de aumento aplicado foi: {percentual_de_aumento_1:.2f} ou 20%')
    print(f'O valor do aumento foi de: {valor_do_aumento_1:.2f} R$')
    print(f'Seu novo salário após o aumento: {reajuste_salarial_1:.2f} R$')
elif 280 < salario <= 700:
    print(f'Seu salário é: {salario} R$')
    print(f'O percentual de aumento aplicado foi: {percentual_de_aumento_2:.2f} ou 15%')
    print(f'O valor do aumento foi de: {valor_do_aumento_2:.2f} R$')
    print(f'Seu novo salário após o aumento: {reajuste_salarial_2:.2f} R$')
elif 700 <= salario <= 1500:
    print(f'Seu salário é: {salario} R$')
    print(f'O percentual de aumento aplicado foi: {percentual_de_aumento_3:.2f} ou 10%')
    print(f'O valor do aumento foi de: {valor_do_aumento_3:.2f} R$')
    print(f'Seu novo salário após o aumento: {reajuste_salarial_3:.2f} R$')
elif salario > 1500:
    print(f'Seu salário é: {salario} R$')
    print(f'O percentual de aumento aplicado foi: {percentual_de_aumento_4:.2f} ou 5%')
    print(f'O valor do aumento foi de: {valor_do_aumento_4:.2f} R$')
    print(f'Seu novo salário após o aumento: {reajuste_salarial_4:.2f} R$')
