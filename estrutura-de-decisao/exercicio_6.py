# 6.Faça um Programa que leia três números e mostre o maior deles.
# Como nosso objetivo por hora é treinar estruturas de decisão então isso vai servir.
# Lembrando que existe uma solução bem menor que será mostrada no próximo exercício.

num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo  número: "))
num_3 = float(input("Digite o terceiro número: "))

if num_1 > num_2 and num_1 > num_3:
    print("O primeiro número é o maior =", num_1)
elif num_2 > num_1 and num_2 > num_3:
    print("O segundo número  é o maior =", num_2)
elif num_1 == num_2 == num_3:
    print("Todos os números são iguais")
else:
    print("O terceiro número é o maior = ", num_3)
