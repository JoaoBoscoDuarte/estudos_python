capacidade_atual, aumento_percentual = map(int, input().split())

aumento = (aumento_percentual/100) + 1
calculo = capacidade_atual * aumento
print(int(calculo))
