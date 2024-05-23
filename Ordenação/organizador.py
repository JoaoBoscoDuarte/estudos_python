lista = []
tamanho = int(input('Tamanho da lista: '))

for i in range (tamanho):
    iten = int(input('Insira um número: '))
    lista.append(iten)
    
for i in range(len(lista) - 1):
    for j in range(len(lista) -1):
        primeiro = lista[j]
        segundo = lista[j+1]
    
        if segundo < primeiro:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            print('Elemento mudado')
            print(lista)
            
print(lista)