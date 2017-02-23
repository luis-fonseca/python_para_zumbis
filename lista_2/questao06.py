mensagem = "O programa calcula o salário bruto e os descontos como "
mensagem = mensagem + "Imposto de Renda, INSS, Sindicato. No final "
mensagem = mensagem + "imprime o salário bruto, líquido e cada desconto."
print(mensagem)

print("")
valor_por_hora = float(input("Qual o valor/hora trabalhada: "))
total_de_horas_trabalhadas = int(input("Total de horas trabalhadas: "))

aliquota_ir = 11 / 100
aliquota_inss = 8 / 100
aliquota_sindicato = 5 / 100
 
salario_bruto = valor_por_hora * total_de_horas_trabalhadas

desconto_total_ir = salario_bruto * aliquota_ir
desconto_total_inss = salario_bruto * aliquota_inss
desconto_total_sindicato = salario_bruto * aliquota_sindicato

deducao_total = (desconto_total_ir + desconto_total_inss 
    + desconto_total_sindicato)
salario_liquido = salario_bruto - deducao_total

mensagem = "Valores calculados ... \n"
mensagem = mensagem + "- Salário Bruto: %4.2f \n"
mensagem = mensagem + "- IR (%d%%): %4.2f \n"
mensagem = mensagem + "- INSS (%d%%): %4.2f \n"
mensagem = mensagem + "- Sindicato (%d%%): %4.2f \n"
mensagem = mensagem + "- Salário Líquido: %4.2f \n"

print("")
print(mensagem % (
    salario_bruto, 
    aliquota_ir * 100, desconto_total_ir,
    aliquota_inss * 100, desconto_total_inss,
    aliquota_sindicato * 100, desconto_total_sindicato,
    salario_liquido))
