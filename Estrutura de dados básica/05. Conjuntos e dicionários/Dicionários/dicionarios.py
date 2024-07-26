#Criando dicionários:

pessoa = {
    'Nome': 'Rafael', 
    'Idade': 19
}
print(pessoa['Nome']) #>>> Rafael


pessoa_2 = dict(Nome = "Rafael", Idade = 21)
print(pessoa_2['Nome']) #>>> Rafael

#----------------------------------------------------------------------

#Adicionando e substituindo dados no dicionário:

pessoa_2['Telefone'] = '(84) 9 9966-7889'
pessoa_2['Idade'] = 20
print(pessoa_2)

#----------------------------------------------------------------------

#dicionários aninhados

contatos = {
    'josefreefire@gmail.com': {'Nome': 'José Free Fire', 'Idade': '68', 'Telefone': '99999999'},
    'joseminecraft@gmail.com': {'Nome': 'José Minecraft', 'Idade': '28', 'Telefone': '88888888'},
    'joseroblox@gmail.com': {'Nome': 'José Roblox', 'Idade': '58', 'Telefone': '55555555'},
}

print(contatos['josefreefire@gmail.com']['Nome'])

#----------------------------------------------------------------------

#Interando sobre um dicionário

for i in contatos:
    print(i, contatos[i])