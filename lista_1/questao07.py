# o programa converte uma temperatura em Celsius para Fahrenheit
# F = 9 * C / 5 + 32

print("O programa converte uma temperatura em Celsius para Fahrenheit")

temperatura = float(input("Informe a temperatura em Celsius: "))
fahrenheit = 9 * temperatura / 5 + 32

print("A temperatura em Fahrenheit é %.2f." % fahrenheit)
