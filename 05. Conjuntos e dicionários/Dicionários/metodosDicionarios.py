email = {
    'marquinos@gmail.com': {'nome': 'Jose', 'idade': 17},
    'bosquinho@gmail.com': {'nome': 'Jose', 'idade': 17},
    'gustavo@gmail.com': {'nome': 'Jose', 'idade': 17},
}

#copia: {}.copy()
copia = email.copy()
copia['marquinos@gmail.com'] = {'nome': 'gui'}
print(email['marquinos@gmail.com'])
print(copia['marquinos@gmail.com'])


#criar novos dicionários com valores padrões: {}.fromkey()
chaves = ['a', 'b', 'c']
valor_padrao = 0
dicionario = dict.fromkeys(chaves, valor_padrao)
print(dicionario)  # Saída: {'a': 0, 'b': 0, 'c': 0}


#acessar chave em dicionário: {}.get()
valor = email['marquinos@gmail.com'].get('nome')
print(valor)


#mostras os itens de um dicionário: {}.items()

#retornar as chaves principais: {}.keys

#apagar: {}.pop()

#obter o valor associado a uma determinada chave em um dicionário {}.setdefault()
    #Se a chave não existir no dicionário, ele a adiciona com o valor padrão fornecido e retorna esse valor. Se a chave já existir, ele simplesmente retorna o valor associado a essa chave, sem fazer nenhuma alteração no dicionário.

teste = {'a': 0, 'b': 1, 'c': 2}
print(teste.setdefault('a', 0))
print(teste.setdefault('d', 0))

#Mudar dados: {}.update()
teste.update({'a': 'testeeeee'})
print(teste['a'])

#puxar os valores: {}.values()
print(email.values())

#deletar: del
del email['bosquinho@gmail.com']
print(email)

#apagar: {}.clear()
email.clear()
print(email)