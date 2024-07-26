def somar(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é: {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 20
exibir_resultado(10, 10, subtracao)  # O resultado da operação 0

a = somar
print(a(10, 4)) # 14