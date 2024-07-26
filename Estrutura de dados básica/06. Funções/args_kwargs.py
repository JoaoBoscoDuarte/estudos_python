#args e kwargs são usadaas para passar variáveis de argumentos para alguma função

# *args permite receber variaveis aletorias e captura-las em uma tupla dentro da função
# *kwargs permite passar um valor da forma (chave='valor')



def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)  
    #aplica uma quebra de linhas entra cada tupla
    
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]) 
    #aplica quebra de linha entre cada metadado, primeira letra de cada palavra maiúscula e um loop que percorre os valores com cahve na tupla 'exibir poema', esse loop irá exibir as chaves e seus rescpectivos valores
    
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    #print com a exibição da data,
    # e o texto em formato de tupla(*args)
    # e os meta dados(**kwargs)
    print(mensagem)


exibir_poema(
    'sexta-feira, 20 de Março de 2002',
    
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)