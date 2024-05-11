def verificar_entrada(valor):
  while True:
    if valor >= 0:
      return valor
      break
      
    else:
      valor = int(input('Digite um valor positivo para a quantidade de passos: '))
      continue

quantidade_passos = int(input('Digite a quantidade de passos: '))
valor_positivo = verificar_entrada(quantidade_passos)

def passos(valor_positivo):
  if valor_positivo == 0:
    print('Nenhum passo dado na floresta')
    
  elif valor_positivo == 1:
    print('Explorador: 1 passo')
    
  else:
    contador = 1
    for passo in range(valor_positivo): 
        if contador == 1:
            print(f'Explorador: {passo + 1} passo')
            contador += 1
        
        else:
            print(f'Explorador: {passo + 1} passos')
            
passos(valor_positivo)