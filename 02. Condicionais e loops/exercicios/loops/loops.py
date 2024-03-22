#1
for i in range (1, 11):
    print(i)

#2
for e in range (10, 1, -1):
    print(e)

#3
quant_termos = int(input("Digite a quantidade de termos: "))
inicio = 1
termos = []

for w in range(0, quant_termos):
    w = int(input(f"Termo de número {inicio}: "))
    inicio += 1
    termos.append(w)

calculo = 1
for elementos in termos:
    calculo *= elementos

print(calculo)

#4
entrada = int(input("Insira um número inteiro: "))

for m in range(entrada - 1, 1, -1):
    calculo = entrada * m
    entrada = calculo

print(entrada)

#5
conjunto = []

entradas = int(input('Número: '))
if entradas >= 0:
    while (entradas >= 0):
        entradas = int(input('Número: '))
        conjunto.append(entradas)
else:
    print('FIM')

for k in conjunto:
    if (k % 10 == 0):
        print(f'O número {k} é multiplo de 10!')
    else:
        print('Nenhum número é multiplo de 10')
        break

#6
numeroCord = int(input("Escreva o número de cordenadas "))
vetor = []

for x in range (numeroCord):
    cordenada = int(input("Escreva as sua cordenada: "))
    vetor.append(cordenada)

vetor_positivo = []
for z in range(len(vetor)):
    if vetor[z] >= 0:
        vetor_positivo.append(True)
    else:
        vetor_positivo.append(False)
        
positivo = all(vetor_positivo)
if positivo != True:
    print("Esse vetor NÂO se encontra no ortante positivo")
else:
    print("Esse vetor SE ENCONTRA NA ORTANTE POSITIVA")

#7
quantidade_provas = int(input('Insira a quantiade de provas:'))

notas_provas = []
for p in range(quantidade_provas):
    nota = float(input(f'Insira a nota da prova {p+1}: '))
    notas_provas.append(nota)

grau = []
for j in range (len(notas_provas)):
    if (notas_provas[j]) >= 5:
        grau.append(True)
    else:
        grau.append(False)

condicao = all(grau)
print(grau)

soma = 0
for z in notas_provas:
    soma += z
    media = soma / len(notas_provas)

if (media >= 7 and condicao == True):
    print(f'A média final é: {media}; O grau é igual ou superior a 5. O candidato está apto a prosseguir')
    
elif (media < 7 and condicao == True):
    print(f'A média final é: {media}; O grau é igual ou superior a 5. O candidato NÂO está apto a prosseguir')
    
elif(media >= 7 and condicao == False):
    print(f'A média final é: {media}; O grau é inferior a 5. O candidato NÂO está apto a prosseguir')

else:
    print(f'A média final é: {media}; O grau é inferior a 5. O candidato NÂO está apto a prosseguir')