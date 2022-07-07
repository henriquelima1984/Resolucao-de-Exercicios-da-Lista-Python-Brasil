# 5.Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros
# formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
# que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto
# sobre vendas.

print()
print('Calculando imposto sobre produtos')
print()


def soma_imposto(taxa_imposto, acrescimo):
    valor_produto_sem_taxa = float(taxa_imposto)
    valor_produto_com_taxa = valor_produto_sem_taxa + (valor_produto_sem_taxa * acrescimo / 100)
    return f'''Valor do produto sem taxa = {valor_produto_sem_taxa:.2f} R$
Valor do produto com taxa = {valor_produto_com_taxa} R$'''


# Aqui você deve informar o valor da mercadoria e a taxa sobre o produto.
print(soma_imposto(100, acrescimo=10))
