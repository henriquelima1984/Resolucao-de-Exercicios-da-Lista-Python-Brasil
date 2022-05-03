# 7. Faça um programa que leia 5 números e informe o maior número.

max_number = None
print()
for i in range(5):
    x = float(input('Informe o ' + str(i + 1) + 'º' + ' número: ' + '\n'))
    max_number = max_number if max_number is not None and max_number > x else x
print()
print('O maior valor digitado foi {} '.format(max_number))
