# o programa calcula quantos segundos existem em um
# determinado intervalo de tempo

print("O programa calcula a quantidade de segundos em um intervalo de tempo")

dias_usuario = float(input("Quantidade de dias: "))
horas_usuario = float(input("Quantidade de horas: "))
minutos_usuario = float(input("Quantidade de minutos: "))
segundos_usuario = float(input("Quantidade de segundos: "))

horas_por_dia = 24
minutos_por_hora = 60
segundos_por_minuto = 60

segundos_por_dia = segundos_por_minuto * minutos_por_hora * horas_por_dia
segundos_por_hora = segundos_por_minuto * minutos_por_hora

segundos_por_dias_calculado = dias_usuario * segundos_por_dia
segundos_por_hora_calculado = horas_usuario * segundos_por_hora
segundos_por_minuto_calculado = minutos_usuario * segundos_por_minuto

segundos_totais = segundos_por_dias_calculado \
    + segundos_por_hora_calculado \
    + segundos_por_minuto_calculado \
    + segundos_usuario

print("O total de segundos calculados foi %.2f" % segundos_totais)

