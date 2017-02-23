# o programa calcula se os valores informados podem ser um triângulo e,
# se for, qual tipo de triângulo é

print("O programa calcula se os valores informados pode ser um triângulo e")
print("identica qual tipo de triângulo é: equilátero, isósceles ou escaleno.")

lado1 = float(input("Informe o primeiro lado: "))
lado2 = float(input("Informe o segundo lado: "))
lado3 = float(input("Informe o terceiro lado: "))

'''
    Um triângulo para ser válido precisa:
    |b - c| < a < b + c
    |a - c| < b < a + c
    |a - b| < c < a + b
'''

if ((lado1 > abs(lado2 - lado3) and lado1 < (lado2 + lado3)) 
    and (lado2 > abs(lado1 - lado3) and lado2 < (lado1 + lado3))
    and (lado3 > abs(lado1 - lado2) and lado3 < (lado1 + lado2))):
    
    if lado1 == lado2 and lado1 == lado3:
        print("Os valores fornecidos formam um triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Os valores fornecidos formam um triângulo isósceles.")
    else:
        print("os valores fornecidos formam um triângulo escaleno.")

else:
    mensagem = "É impossível, com os valores informados, a existência "
    mensagem = mensagem + "de um triângulo."
    print(mensagem)


