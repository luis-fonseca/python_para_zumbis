# !/usr/bin/python3
import math

mensagem = "O programa calcula, dado o tamanho da área em m2, a "
mensagem = mensagem + "quantidade de latas de tinta necessárias "
mensagem = mensagem + "e o preço total a ser pago."
print(mensagem)

print("")

tamanho_da_area = float(input("Informe o tamanho da área em m2: "))

litros_por_lata = 18
cobertura_por_litro = 3 # 3/m2
cobertura_total_por_lata = litros_por_lata * cobertura_por_litro
preco_por_lata = 80.00

total_de_latas = tamanho_da_area / cobertura_total_por_lata
total_de_latas = math.ceil(total_de_latas)
custo_total = total_de_latas * preco_por_lata

print("")

mensagem = "Valores computados: \n"
mensagem = mensagem + "- Total de latas de tinta necessárias: %d. \n"
mensagem = mensagem + "- Custo total: %4.2f."
print(mensagem % (total_de_latas, custo_total))