#Os conjutos são usados para realizar operçãoes do mundo matemático, dos conjuntos numéricos
#UNIÃO (union):
a = {1, 2, 3}
b = {1, 2, 4}

print(a.union(b))


#INTERSECÇÂO DE CONJUTOS (Intersection)
print(a.intersection(b))


#DIFERENÇA (difference)
print(a.difference(b))


#DIFERENÇA SIMÉTRICA (symmetric_difference)
print(a.symmetric_difference(b))


#SUBCONJUNTOS (issubst)
c = {1, 2, 3}
d = {1, 2, 3, 4, 5 , 6}

print(c.issubset(d))


#NÃO É SUBCONJUNTO (isdisjoint)
e = {1, 3, 5}
f = {2, 4, 6}

print(e.isdisjoint(f))


#ADICIONAR
e.add(7)
print(e)


#REMOVER
e.remove(7)
print(e)


#DESCARTAR
e.discard(1)
print(e)


#Remover o último elelemento
e.pop()
print(e)