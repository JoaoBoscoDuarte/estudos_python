def main():
    taxaDeServico = 0.12

    while True:
        valorConta = input("Insira o valor da conta: ")

        if not valorConta.isdigit():
            print("Insira um valor válido")
            continue

        valorConta = float(valorConta)
        taxaGarcon = taxaDeServico * valorConta
        print(f"A taxa do garçon é R$: {taxaGarcon:.2f} e valor total da conta acrescido da taxa é de: R${valorConta + taxaDeServico}")
        break

main()