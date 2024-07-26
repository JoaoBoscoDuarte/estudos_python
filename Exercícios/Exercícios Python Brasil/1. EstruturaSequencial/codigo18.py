#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = float(input('Digite o tamanho do arquivo (em MB): '))
velocidade = float(input('Digite a velocidade da internet (em Mbps)'))

segundos = (tamanho_arquivo * 8) / velocidade
minutos = segundos / 60
print(f'Levará: {minutos} minutos')