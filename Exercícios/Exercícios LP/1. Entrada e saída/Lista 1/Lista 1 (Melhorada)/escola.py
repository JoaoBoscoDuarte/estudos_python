def main():
    valorProjeto = 80
    valorHoraAula = 35

    while True:

        quantProjetos = input("Insira a quantidade de projetos orientados: ")

        if not quantProjetos.isdigit():
            print("Insira um valor válido")
            continue

        horasDeAula = input("Insira a quantiade de horas em sala de auala: ")

        if not horasDeAula.isdigit():
            print("Insira um valor válido")
            continue
        
        quantProjetos = int(quantProjetos)
        horasDeAula = int(horasDeAula)
        valorDeAula = valorHoraAula * horasDeAula
        valorProjetoPagar = valorProjeto * quantProjetos
        print(f"O valor total a pagar para esse professor é: {valorDeAula + valorProjetoPagar:.2f}")
        break
        
main()