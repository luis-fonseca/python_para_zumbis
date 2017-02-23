#! /usr/bin/python3

print("O programa lê 3 números e mostra qual o maior.")

maior = 0

n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))
n3 = float(input("Informe o terceiro número: "))


if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

mensagem = "O maior número é %d."
print(mensagem % maior)
