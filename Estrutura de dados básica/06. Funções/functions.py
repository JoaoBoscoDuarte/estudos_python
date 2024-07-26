def olaMundo ():
    print('Ola mundo')
    
olaMundo() #>>> Ola mundo

#-----------------------------------------

def seuNome (nome):
    print(f'bem vindo {nome}')
    
seuNome('Jose')

#------------------------------------------

def seuOutroNome (nome='usuário'):
    print(f'Bem vindo {nome}')

seuOutroNome() #>>> Bem vindo usuário

def seuOutroOutroNome (nome):
    print(f'Bem vindo {nome}')

seuOutroNome(nome='felipe') #>>> Bem vindo felipe

#------------------------------------------

def soma (numeros):
    return sum(numeros)
    
print(soma([1, 2, 5]))

#------------------------------------------

