#CONJUNTO = Coleção de objetos sem elementos repitidos, funciona como um conjunto matemático (sets)

print(set('abacaxi')) #>>> {'x', 'a', 'i', 'c', 'b'}

numeros = [1, 3, 4, 4, 1, 6, 7, 1, 7]
print(set(numeros)) #>>> {1, 3, 4, 6, 7}



#Acessando valores:
conjunto = set({1, 3, 4, 5, 11, 3, 5, 2, 3, 1, 6, 7})
conjuntos = list(conjunto)
print(conjuntos[0]) #>>> 1



#Interando conjuntos:
for i in conjunto:
    print(i) #>>> Saída sem os itens duplicados