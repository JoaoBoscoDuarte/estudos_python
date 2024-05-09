aleatorio = 'Essa mensagem aleatoria'

print(aleatorio[0]) #>> 'E'
print(aleatorio[:]) #>> 'Essa mensagem aleatoria'
print(aleatorio[:9]) #>> 'Essa mens'
print(aleatorio[0:4]) #>> 'Essa'
print(aleatorio[5:]) #>> 'mensagem aleatoria'
print(aleatorio[5:13]) #>> 'Mensagem'
print(aleatorio[::2]) #>> 'Es esgmaetra'; dado determinado intervalo (::), print desse intervelo em 2 em 2
print(aleatorio[-1]) #>> 'a'
print(aleatorio[::-1]) #>> 'airotaela megasnem assE'



#Strings de multiplas linhas:
name = '''
Olá, eu me chamo Rafael;
Sou de Piraciguagapipina;
'''

print(name)