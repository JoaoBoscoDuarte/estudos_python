#A empresa Realeza está investindo em um programa para melhorar a qualidade de vida de seus funcionários. Para isso, concederá a cada funcionário um ingresso para uma partida do campeonato paraibano de futebol, e para cada funcionária um ingresso para o cinema. Além disso, caso o(a) funcionário(a) seja casado(a), receberá um ingresso para seu companheiro(a).Todos aqueles que tenham filhos receberão também um ingresso para cada um deles. Escreva um programa que receba como entrada o sexo, o estado civil e a quantidade de filhos de um funcionário e exiba uma mensagem indicando o tipo de ingresso ganho e a quantidade. Obs: o cônjuge e os filhos recebem o mesmo tipo de ingresso do (a) funcionário (a), não importando seus sexos. Além disso, existem vários estados civis, mas apenas funcionários (as) casados(as) receberão ingressos para seus cônjuges.

sexo = input("Insira o sexo: ").lower()
quantIngresso = 0

if (sexo == "feminino"):
	quantIngresso += 1
	tipoDeIngresso = "cinema"

	estadoCivil = input("Insira o seu estado civil: ")

	if (estadoCivil == "solteira"):
		perguntaFilhos = input("Você tem filhos: ").lower

		if (perguntaFilhos == "sim"):
			quantFilhos = int(input("Insira a quantidade de filhos: "))
			quantIngresso += quantFilhos
			print(f"O tipo de ingresso escolhido foi: Feminino, solteira com {quantFilhos}, logo você receberá {quantIngresso} para o {tipoDeIngresso}")

		else:
			print(f"O tipo de ingresso escolhido foi: Faminino, solteira, sem filhos, logo você receberá: {quantIngresso} para o {tipoDeIngresso}")

	else:
		quantIngresso += 1

		perguntaFilhos = input("Você tem filhos?: ").lower()

		if (perguntaFilhos == "sim"):
			quantFilhos = int(input("Insira a quantidade de filhos: "))
			quantIngresso += quantFilhos

			print(f"O tipo de ingresso escolhido foi: Feminino, casada com {quantFilhos}, logo você receberá {quantIngresso} para o {tipoDeIngresso}")

		else:
			print(f"O tipo de ingresso escolhido foi: Faminino, casada, sem filhos, logo você receberá: {quantIngresso} para o {tipoDeIngresso}")

else:
	quantIngresso += 1
	tipoDeIngresso = "futebol"

	estadoCivil = input("Insira o seu estado civil: ")

	if (estadoCivil == "solteiro"):
		perguntaFilhos = input("Você tem filhos: ").lower()

		if (perguntaFilhos == "sim"):
			quantFilhos = int(input("Insira a quantidade de filhos: "))
			quantIngresso += quantFilhos
			print(f"O tipo de ingresso escolhido foi: Feminino, solteira com {quantFilhos}, logo você receberá {quantIngresso} para o {tipoDeIngresso}")

		else:
			print(f"O tipo de ingresso escolhido foi: Masculino, solteiro, sem filhos, logo você receberá: {quantIngresso} para o {tipoDeIngresso}")

	else:
		quantIngresso += 1

		perguntaFilhos = input("Você tem filhos: ").lower

		if (perguntaFilhos == "sim"):
			quantFilhos = int(input("Insira a quantidade de filhos: "))
			quantIngresso += quantFilhos
			print(f"O tipo de ingresso escolhido foi: Masculino, casado com {quantFilhos}, logo você receberá {quantIngresso} para o {tipoDeIngresso}")

		else:
			print(f"O tipo de ingresso escolhido foi: Masculino, casad, sem filhos, logo você receberá: {quantIngresso} para o {tipoDeIngresso}")
