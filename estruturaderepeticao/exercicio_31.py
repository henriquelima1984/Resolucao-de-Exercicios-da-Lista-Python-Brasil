preco = float(input("Preço do pão: "))
print("Panificadora Pão de Ontem - Tabela de preços")
for i in range(1, 51):
    print(f"{i:2d} - R$ {preco*i:5.2f}")
