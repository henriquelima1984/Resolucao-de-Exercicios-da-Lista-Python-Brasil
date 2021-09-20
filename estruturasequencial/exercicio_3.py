"""

3. Faça um Programa que peça dois números e imprima a soma.

Você pode fazer assim

>>> soma = num1 + num2
>>> print(soma)

"""

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

#Ou pode fazer a operação dessa forma eliminando a variável soma
num1 += num2

print(num1)