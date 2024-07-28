#Os preços abaixo são da cantina da empresa onde Thomas trabalha. Sabendo que aqueles que comprarem mais de 3 bebidas ganham uma fatia de bolo, escreva um programa que receba como entrada o tipo e a quantidade de bebida escolhida por um cliente e exiba o valor total a pagar e uma mensagem indicando se ele ganhou o bolo ou não.

cafe = 2.50
suco = 3.50
refrigerante = 4.05

tipoBebida = input("Insira o tipo de bebida [cafe], [suco], [refrigerante]: ")
quantBebida = int(input("Insira a quantidade de bebida: "))

if (tipoBebida == "cafe"):
	if (quantBebida > 3):
		print(f"O preçoa se pagar é: {cafe * quantBebida:.}, voê ganhou um bolo gratis")
	else:
		print(f"O preço a se pagar é: {cafe * quantBebida:.2f}")

elif (tipoBebida == "suco"):
	if (quantBebida > 3):
		print(f"O preço a se pagar é: {suco * quantBebida:.2f},  voê ganhou um bolo gratis")
	else:
		print(f"O preço a se pagar é: {cafe * quantBebida:.2f}")

else:
	if (quantBebida > 3):
		print(f"O preçoa se pagar é: {refrigerante * quantBebida:.2f}, voê ganhou um bolo gratis")
	else:
		print(f"O preço a se pagar é: {refrigerante * quantBebida:.2f}")