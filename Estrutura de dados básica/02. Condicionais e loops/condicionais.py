#estrutura condicionais

numero = int(input('Escreva um número'))

#se o numero(input) for maior ou menor que 5 e também for menor ou igal a 10 >>>print aquele texto
if numero >= 5 and numero <= 10:
    print(f'O número está entre 5 e 10')

#e se, o número (input) for maior ou menor que 4 e também for menor que 5 >>>print aquele texto ali
elif numero >= 0 and numero < 5:
    print(f'O número está entre entre 0 e 4')

#se não, printa isso aí
else:
    print('Número fora de intervalo definido')


#If ternário (realizado em uma única linha)
saque = 200
saldo = 800
status = 'Sucesso' if saque <= saldo else 'falha'

print(f'{status} ao realizar o saque')