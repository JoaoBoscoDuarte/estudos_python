#Dicionar elemento:
lista = ['Sei', 'não', 'nada', 'jose', 'não']
lista.append('Cachorro')
print(lista)

#copia lista
novaLista = lista.copy()
print(novaLista)

#Limpar tudo:
lista.clear()
print(lista)

#Quantos elementos iguais em uma lista
print(novaLista.count('nada'))
print(novaLista.count('não'))

#juntar listas
linguagens = ['javascript', 'python', 'Csharp']
linguagens.extend(['C', 'C++', 'Java', 'Rust'])
print(linguagens)

#Puxar o índex de um elemento
print(linguagens.index('Java'))

#pegar o último elemento da lista:
print(linguagens.pop())

#Remover determinado elemento
linguagens.remove('Csharp')
print(linguagens)

#Inverter lista
linguagens.reverse()
print(linguagens)

#Ordenar elementos por ordem alfabética ou numérica
linguagens.sort() #ordem numérica ou alfabética
print(linguagens)

linguagens.sort(reverse=True) #ordem alfabética ou númerica iversa
print(linguagens)

linguagens.sort(key=lambda x:len(x)) #Pela quantidade de letras por palavra
print(linguagens)

linguagens.sort(key=lambda x:len(x), reverse=True) #Pela quantidade de letras por palavra (Inversa)
print(linguagens)