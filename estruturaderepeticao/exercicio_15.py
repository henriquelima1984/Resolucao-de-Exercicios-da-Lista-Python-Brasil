# 15.A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série
# até o n−ésimo termo.

# OBS: Fibonacci é uma sequência infinita de números naturais

print()
num = int(input('Termos da sequência de Fibonacci: '))
f1 = 0
f2 = 1
f3 = 0

while f2 < num:
    if f2 < 2:
        print(f3, end=', ')
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f3, end=', ')
