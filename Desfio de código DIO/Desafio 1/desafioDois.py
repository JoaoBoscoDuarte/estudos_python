# Lista para armazenar os itens
itens = []

for i in range(3):
    entrada = input('Digite o iten que deseja cadastrar: ')
    itens.append(entrada)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")