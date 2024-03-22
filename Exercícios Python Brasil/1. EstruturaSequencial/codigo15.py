'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    a)salário bruto.
    b) quanto pagou ao INSS.
    c) quanto pagou ao sindicato.
    d) o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
---------------------------
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
---------------------------
'''

quanto_por_hora = float(input("Quanto você ganha por hora:"))
quant_horas_trabalhadas = float(input("Quantidade de horas trabalhadas por mês:"))
casas_decimais = 2

calculo_inicial = (quanto_por_hora * quant_horas_trabalhadas)
calculo_total = calculo_inicial - (0.11 * calculo_inicial) - (0.08 * calculo_inicial) - (0.05 * calculo_inicial)
print('Salário Liquido: {:.{}f}'.format(calculo_total, casas_decimais))