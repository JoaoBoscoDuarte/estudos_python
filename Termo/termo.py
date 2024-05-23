import random

def main ():
    dicionario = ['amor', 'corinthians', 'verdade', 'saxofone', 'trombonea', 'trompetea', 'galinha', 'cavalo']
    palavra_aleatoria = random.choice(dicionario)
    desenho = len(palavra_aleatoria) * '_'

    def inicio ():
        print('Seja bem vindo ao TERMO, jogo de adivinhação de palavras')
        inicio = input('Você deseja iniciar o jogo?: ').lower()
        
        while True:
           if inicio != 'não' or inicio != 'sim':
               if inicio == 'sim':
                   game(desenho)
                   break
               elif inicio == 'não':
                   print('FIM')
                   break
               else:
                   inicio = input('Por favor, responda com sim ou não: ')
                   continue
           else:
               inicio = input('Você deseja iniciar o jogo?: ')
        
    def game(desenho):
        print(f'A palavra aleatória contem {len(palavra_aleatoria)} letras')
        print(desenho)
        
        letras_usadas = []
        tentativas = 3
        
        while True:
            sugestao = input('Surgira uma letra: ').lower()
            
            if len(sugestao) != 1 or not sugestao.isalpha():
                sugestao = input('Por favor, sugira uma letra: ')
                continue
            
            if sugestao in palavra_aleatoria:
                for i in range(len(palavra_aleatoria)):
                    if palavra_aleatoria[i] == sugestao:
                        desenho_lista = list(desenho)
                        desenho_lista[i] = sugestao
                        desenho = ''.join(desenho_lista)
                        
                letras_usadas.append(sugestao)
                print(desenho)
                print(f'Essa letra pertence a palavra, lista de letras usadas: {letras_usadas}')
                vamos_tentar()
            
            elif sugestao in letras_usadas:
                print(f'Essa letra já foi usada letras usadas: {letras_usadas}')
                vamos_tentar()
                
            else:
                print(desenho)
                print(f'Essa letra não pertence a palavra, lista de lestras utilizadas: {letras_usadas}')
                letras_usadas.append(sugestao)
                vamos_tentar()
            
            if desenho == palavra_aleatoria:
                print(desenho)
                print(f'Parabéns, você acertou a palavra [{palavra_aleatoria}]')
                break
            
            def vamos_tentar():
                tentativa = input('Você deseja continuar ou quer arriscar uma tentativa (3 restantes)? [Continuar] ou [Arriscar]')
                
                while True:
                    tentativa.lower()
                    if tentativa == 'continuar':
                        game(desenho)
                        
                    elif tentativa == 'arriscar':
                        tentativa = tentativa - 1
                        palavra_tentativa = input('Insira a palavra: ')
                        palavra_tentativa.lower
                        
                        if palavra_tentativa == palavra_aleatoria:
                            print(f'Parabéns! você acertou a palvra [{palavra_aleatoria}]')
                            break
                        
                    else:
                        tentativa = input('Você deseja continuar ou quer arriscar uma tentativa (3 restantes)? [Continuar] ou [Arriscar]')
                        continue
                
                    if tentativas < 0:
                        print(f'Você perdeu, a palavra era [{palavra_aleatoria}]')
                        break
            
    inicio()
    
main()