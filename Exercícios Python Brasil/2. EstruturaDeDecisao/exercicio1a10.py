#1. Faça um Programa que peça dois números e imprima o maior deles.
#2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
n1 = int(input("Escreva um número"))
n2 = int(input("Escreva outro número"))

if n1 > n2:
    if n1 >= 0:
        print(f'O maior número é {n1} e positivo')
    else:
        print(f'O maior número é {n1} e negativo')
else:
    if n2 >= 0:
        print(f'O maior número é {n2} e positivo')
    else:
        print(f'O maior número é {n2} e negativo')

#2. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
while True:
    letra = input("Escreva F ou M")
    if letra == 'F':
        print('Feminino, sexo válido')
        break
    elif letra == 'M':
        print('Masculino, sexo válido')
        break
    else: 
        print('Letra inválida')

#3. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
while True:
    letra2 = input('Digite uma letra: ')
    if len(letra2) != 1 or not letra2.isalpha():
        print('Inválido, por favor Digite somente uma letra')
    else:
        if letra2.lower() in ('a', 'e', 'i', 'o', 'u'):
            print('Essa letra é uma Vogal')
            break
        else:
            print('Essa letra é uma consoante')
            break

#11
salario = float(input("Qual o seu salário? "))

if salario <= 280:
    salario2 = salario * 1.2
    print(f'Salario antes do rejuste: {salario:.{2}f}; Percentual de aumento: 20%; Aumento: {(0.2 * salario):.{2}f}; O novo salário é de {salario2:.{2}f}')
elif salario > 280 and salario < 700:
    salario2 = salario * 1.15
    print(f'Salario antes do rejuste: {salario:.{2}f}; Percentual de aumento: 15%; Aumento: {(0.15 * salario):.{2}f}; O novo salário é de {salario2:.{2}f}')
elif salario > 700 and salario < 1500:
    salario2 = salario * 1.1
    print(f'Salario antes do rejuste: {salario:.{2}f}; Percentual de aumento: 10%; Aumento: {(0.1 * salario):.{2}f}; O novo salário é de {salario2:.{2}f}')
else:
    salario2 = salario * 1.05
    print(f'Salario antes do rejuste: {salario:.{2}f}; Percentual de aumento: 5%; Aumento: {(0.05 * salario):.{2}f}; O novo salário é de {salario2:.{2}f}')