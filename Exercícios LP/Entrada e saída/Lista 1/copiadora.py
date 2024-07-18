def main():
    copia = 0.15

    while True:
        quantFolhas = input("Insira a quantidade de folhas")

        if not quantFolhas.isdigit():
            print("Insira um número inteiro de folhas que deseja imprimir")
            continue

        quantFolhas = int(quantFolhas)
        paginas = quantFolhas * 2
        calculo = paginas * copia
        print(f"O valor da impressão de {quantFolhas} é: R${calculo:.2f}")
        break

main()