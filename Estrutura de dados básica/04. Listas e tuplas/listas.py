lista = ['Matemática discreta', 'Introdução a computação', 'Introdução a programação']
print(lista[1]) #>>> 'Introdução a computação'
print(lista[-1]) #>>> 'Introdução a programação'

#MATRIZ ALINHADA
matriz = [
    [0, 'a', 1],
    [2, 4, 'b'],
    ['a', 1, 0],
]

print(matriz[0]) #>>> [0, 'a', 1]
print(matriz[0][0]) #>>> 0
print(matriz[1][2]) #>>> 'b'

#PODE-SE FATIAR LISTAS

#INTERANDO LISTAS:
#Pelos número de elementos
for i in range(len(lista)):
    print(lista[i])

#Por cada elemento de uma lista:
for j in lista:
    print(j)

#COMPRENSSÃO DE LISTAS:
numeros = [1, 3, 4, 6, 36, 64]
pares = []

for i in numeros:
    if i % 2 == 0:
        pares.append(i)

print(pares)

#compreesa:
pares = [n for n in numeros if n % 2 == 0]
print(pares)