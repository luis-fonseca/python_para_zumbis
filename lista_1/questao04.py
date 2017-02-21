# O programa calcula a porcentagem de aumento de um salário

print("O programa calcula a porcentagem de aumento e o novo salário.\n")
salario = float(input("Informe o seu salário: "))
porcentagem_do_aumento = float(input("Informe a porcentagem de aumento: "))

porcentagem_do_aumento = porcentagem_do_aumento / 100
valor_do_aumento = salario * porcentagem_do_aumento
novo_salario = salario + valor_do_aumento

print("O valor do aumento foi de %.2f. O novo salário é de %.2f" % \
      (valor_do_aumento, novo_salario))
