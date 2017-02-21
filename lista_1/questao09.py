# O programa calcula o preço a pagar dados os dias de aluguel e
# combustível consumido pelo carro

print("O programa calcula o preço a pagar pelos dias de aluguel e \
combustível consumido.")

custo_por_quilometro = 0.15
custo_por_dia_aluguel = 60

quilometros_percorridos = float(input(
    "Quantos quilometros percorreu com o carro: "))
dias_alugado = int(input("Por quanto dias o carro foi alugado: "))

custo_total_quilometro = quilometros_percorridos * custo_por_quilometro
custo_total_aluguel = dias_alugado * custo_por_dia_aluguel

custo_total = custo_total_quilometro + custo_total_aluguel

print("O custo total foi de %.2f" % custo_total)
