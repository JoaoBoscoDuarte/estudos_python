#parametros por posição
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    #Posição separada pela barra (/), as posições modelo, ano e placa não devem conter chaves, marcas, motor e combustível sim
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

#-----------------------------------------------------------------------------------------------------------------------------------

#parametros por nome
def criar_carro_2(*, modelo, ano, placa, marca, motor, combustivel):
    #observe o '*' no início, iss significa que a função só irá aceitar valores com chave
    print(modelo, ano, placa, marca, motor, combustivel)

# criar_carro_2("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido
criar_carro_2(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#-----------------------------------------------------------------------------------------------------------------------------------

#Misto, apresenta os dois tipos de passagem

def criar_carro_3(modelo, ano, placa, /, marca, motor, *, combustivel):
    #Posição separada pela barra (/), as posições modelo, ano e placa não devem conter chaves, marcas, motor e combustível sim
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_3("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
