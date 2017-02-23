# o programa verifica se um determinado ano é bissexto

print("O programa verifica se um ano é bissexto.")

ano = int(input("Digite o ano para verificar se é um ano bissexto: "))
mensagem = ""

if ((ano % 4 == 0 and ano % 100 != 0) 
    or (ano % 100 == 0 and ano % 400 == 0)):
    mensagem = "O ano %s é um bissexto."
else:
    mensagem = "O ano %s não é um bissexto."

print(mensagem % ano)