def main():
    multaPorDia = 2.5

    while True:
        quantDias = input("Insira a quantidade de dias de atraso: ")

        if not quantDias.isdigit():
            print("Insira um valor inteiro para a qauntidade de dias!")
            continue

        quantDias = int(quantDias)
        calculo = multaPorDia * quantDias
        print(f"O valor que você terá que pagar para a multa de {quantDias} é: R${calculo:.2f}")

main()