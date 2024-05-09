#Tuplas são parecidas com listas, a diferença é que são imutáveis

#Exemplo de tuplas:
frutas = ('Maçã', 'banana', 'Goiaba',)

linguagens = tuple('Python')

numeros = tuple([1, 2, 3, 4, 5])

paises = ('Brasil',)

# => Utiliza-se tuplas quando você não deseja que valor seja mudado

#Interando tuplas:
for fruta in range(len(frutas)):
    print(fruta)
    
#função enumerate:
for indice, fruta in enumerate(frutas):
    print(f'a fruta {fruta}, apresenta índice {indice}')
    
#METODOS:
'''
().count
().index
len()
'''