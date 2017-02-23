print("O programa calcula o rendimento diário e multa de um pescador.")

valor_multa_por_quilo = 4.00
limite_quilos_diario = 50
multa, excesso = 0, 0

peso = float(input("Informe o peso total: "))

if peso > limite_quilos_diario:
    excesso = peso - limite_quilos_diario
    mensagem = "Você ultrapassou o limite diário em %5.2f e "
    mensagem = mensagem + "por isso a multa será de %5.2f."
    multa = excesso * valor_multa_por_quilo
else:
    mensagem = "O excesso foi %5.2f e a multa foi %5.2f. "
    mensagem = mensagem + "Você está dentro do limite diário."

print(mensagem % (excesso, multa))
