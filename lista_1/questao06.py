# o programa calcula o tempo de viagem de carro
print("O programa calcula o tempo de viagem de carro com base na distância \
e velocidade média.")

distancia = float(input("Distância a percorrer: "))
velocidade_media = float(input("Qual a velocidade média: "))

# v = s / t
# 90t = 180 => 180 / 90 => 2
tempo = distancia / velocidade_media

print("O tempo estimado de viagem são de %.2f horas" % tempo)
