# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes. 

print('-'*32)
print('Senso Academia Smart Fit Nutella')
print('-'*32)

codigo_cliente_mais_gordo = 0
codigo_cliente_mais_magro = 0
codigo_cliente_mais_alto = 0
codigo_cliente_mais_baixo = 0

maior_altura = 0
menor_altura = 2.72
maior_peso = 0
menor_peso = 595

media_das_alturas = 0
media_dos_pesos = 0
soma_das_alturas = 0
soma_dos_pesos = 0
qtd_clientes = 0

print()
while True:
  codigo = int(input('Informe seu código: '))
  if codigo == 0:
    break
  qtd_clientes += 1
  altura_do_cliente = float(input('Informe sua altura: '))
  peso_do_cliente = float(input('Informe seu peso: '))

  soma_das_alturas += altura_do_cliente 
  soma_dos_pesos += peso_do_cliente

  if altura_do_cliente > maior_altura:
    maior_altura = altura_do_cliente
    codigo_cliente_mais_alto = codigo
  
  if altura_do_cliente < menor_altura:
    menor_altura = altura_do_cliente
    codigo_cliente_mais_baixo = codigo
  
  if peso_do_cliente > maior_peso:
    maior_peso = peso_do_cliente
    codigo_cliente_mais_gordo = codigo
  
  if peso_do_cliente < menor_peso:
    menor_peso = peso_do_cliente
    codigo_cliente_mais_magro = codigo

    media_das_alturas = soma_das_alturas / qtd_clientes
    media_dos_pesos = soma_dos_pesos / qtd_clientes

print()
print(f"""Cliente mais alto tem {maior_altura:.2f} m
Cliente mais baixo tem {menor_altura:.2f} m
Cliente mais gordo tem {maior_peso:.2f} kg
Cliente mais magro tem {menor_peso:.2f} kg
Média de altura é {media_das_alturas:.2f} m
Média de peso é {media_dos_pesos:.2f} kg""")
