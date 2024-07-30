def isDecimal(a):
    if a.count(".") > 1:
        return False
    
    if a.replace(".", "", 1).isdigit():
        return True
    
    return False

def main():
    while True:
        taxaDeCambio = input("Insira a taxa de cambio")

        if not isDecimal(taxaDeCambio):
            print("Insira um valor válido")
            continue

        valor = input("Insira o valor que deseja converter")

        if not isDecimal(valor):
            print("Insira um valor válido")
            continue

        taxaDeCambio = float(taxaDeCambio)
        valor = float(valor)
        convert = valor/taxaDeCambio

        print(f"O valor convertido em dolares é de {convert}")
        break

main()