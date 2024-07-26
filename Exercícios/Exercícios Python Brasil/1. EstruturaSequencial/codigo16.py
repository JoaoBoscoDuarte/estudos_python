"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

tamanho = float(input("digite o tamanho em mestros:"))
quant_litros = tamanho/3
quant_latas = 0

if ((quant_litros % 18) > 0):
    quant_latas += 1

preco_total = quant_latas * 80

print(f'A quantidade de latas de tinta:{quant_latas}; \n Preço: {preco_total}')


