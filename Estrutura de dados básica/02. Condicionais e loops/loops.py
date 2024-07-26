#Estruturas de repetição

#for interável
texto = input('Insira uma palavra:')
vogais = 'AEIOU'

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end='')
else:
    print()

#for range
'''
    for i in range(inicio, fim, passo):
'''

lista = [1, 3, 5, 6, 8, 11]

for indices in range (len(lista)):
    print(indices)


#While (enquanto)
opcao = input('Insira um número:')

while opcao != '0':
    if opcao == '1':
        print("Te amo")
        break
    elif opcao == '2':
        print("tomate cru")
        break
    else:   
        print("Valor inválido")
        opcao = input('tente 1 ou 2. 0 para sair. ')