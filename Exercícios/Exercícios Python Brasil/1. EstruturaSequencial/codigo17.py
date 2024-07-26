'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
import math

tamanho = float(input("Digite o tamanho em mestros quadrados:"))
quantidade_tinta = tamanho/6

#apenas lata de 18
quant_latas = math.ceil(quantidade_tinta / 18)
preco_total_latas = quant_latas * 80

#apenas galão
quant_galao = math.ceil(quantidade_tinta / 3.6)
preco_total_galao = quant_galao * 25

#variável
quant_latas_mista = int(quantidade_tinta / 18) 
quant_galao_mista = math.ceil((quantidade_tinta % 18) / 3.6)

preco_total_misto = (quant_latas_mista * 80) + (quant_galao_mista * 25)

print(f'Quantidade de tinta a ser comprada (apenas latas): {quant_latas}, Preço total: R$ {preco_total_latas:.2f}')
print(f'Quantidade de tinta a ser comprada (apenas galões): {quant_galao}, Preço total: R$ {preco_total_galao:.2f}')
print(f'Quantidade de tinta a ser comprada (misturando latas e galões): {quant_latas_mista} latas e {quant_galao_mista} galões, Preço total: R$ {preco_total_misto:.2f}')