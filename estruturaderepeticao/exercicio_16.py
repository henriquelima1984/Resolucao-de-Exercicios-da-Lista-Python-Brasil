# 16.A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34...
# Faça um programa que gere a série até que o valor seja maior que 500.

num = int(input('Termos da sequência de Fibonacci: '))
f1 = 0
f2 = 1
f3 = 0

for _ in range(num):
    if f2 < 2:
        print(f3, end=' ')
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f3, end=' ')
