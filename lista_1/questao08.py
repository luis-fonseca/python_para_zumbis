# o programa converte uma temperatura em Fahrenheit para Celsius
# C = (F - 32) / 1.8

print("O programa converte uma temperatura em Fahrenheit para Celsius.")

temperatura = float(input("Informe a temperatura em Fahrenheit: "))
celsius = (temperatura - 32) / 1.8

print("A temperatura em Celsius é %.2f." % celsius)
