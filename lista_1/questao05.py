# o programa calcula o percentual de desconto e imprime o preço final

print("O programa calcula o percentual de desconto e imprime \
o preço final de uma mercadoria.")

preco_mercadoria = float(input("Qual o preço da mercadoria: "))
percentual_de_desconto = float(input("Percentual de desconto: "))

percentual_de_desconto = percentual_de_desconto / 100
valor_do_desconto = preco_mercadoria * percentual_de_desconto
preco_final = preco_mercadoria - valor_do_desconto

print("O valor do desconto para a mercadoria: %.2f. \
O valor total a pagar: %.2f" % (valor_do_desconto, preco_final))
