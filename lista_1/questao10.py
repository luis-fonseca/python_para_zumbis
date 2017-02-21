# o programa calcula a redução do tempo de vida de um fumante

print("O programa calcula o total de dias perdidos por um fumante.")

quantidade_de_cigarros = int(input(
    "Informe a quantidade de cigarros fumados por dia: "))
quantidade_de_anos = float(input("Informe a quantidade de anos como fumante: "))

dias_por_ano = 365
segundos_por_minuto = 60
minutos_perdidos_por_cigarro = 10

horas_por_dia = 24
minutos_por_hora = 60
segundos_por_minuto = 60
segundos_por_dia = segundos_por_minuto * minutos_por_hora * horas_por_dia

total_de_cigarros_consumidos = (quantidade_de_anos * dias_por_ano) * quantidade_de_cigarros
total_de_minutos_perdidos_por_cigarro = total_de_cigarros_consumidos \
                                        * minutos_perdidos_por_cigarro

total_de_segundos_perdidos_por_cigarro = total_de_minutos_perdidos_por_cigarro \
                                         * segundos_por_minuto

dias_perdidos_pelo_consumo = total_de_segundos_perdidos_por_cigarro / segundos_por_dia

print("O total de dias perdidos pelo consumo do cigarro foram %.2f" % dias_perdidos_pelo_consumo)


