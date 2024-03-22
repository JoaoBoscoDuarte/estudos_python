#USANDO CONSOLE
print ("Artie joga muito dark souls"); 
print (2 + 2)
print (2 * 2)
print (2 / 2)
print (2 - 2)

#USANDO VARIÁVEIS:
nome = "João Bosco"
idade = 17
hobbie = "escutar musga"
print (f"O {nome}, que tem {idade}, gosta muito de {hobbie}")

#USANDO input, chama uma entrada com mensagem personalizada
nome = input ("Qual o seu nome?")
idade = int(input("Digite sua idade"))  #int --> número inteiro;
peso = float(input ("Qual o seu peso"))  #float --> número flutuante, decimal

print (f"O {nome}, que tem {idade}, e pesa {peso}")

#OUTROS TIPOS DE VARIÁVEIS:
string = "Olá, mundo!" #srt --> texto
booleano = True #bool --> O tipo booleano é utilizado para representar valores lógicos, ou seja, verdadeiro ou falso.
complexo = 10 + 5j # --> O tipo complexo é utilizado para representar números complexos

lista = [1, 2, 3, 4, 5] # ---> O tipo lista é utilizado para representar uma coleção de valores.
lista.remove(3) #Remove um elemento determinado da lista;
lista.append(6) #Adiciona um alemento na lista

tupla = (1, 2, 3, 4, 5) # ---> Assim como as listas, o tipo tupla é utilizado para representar uma coleção de valores. Porém, as tuplas são imutáveis, ou seja, não é possível adicionar, remover ou alterar valores de uma tupla.

dicionario = {"nome": "João", "idade": 20} # ---> O tipo dicionário é utilizado para representar uma coleção de valores. Em Python, um dicionário é composto por pares de chave e valor.

conjunto = {1, 2, 3, 4, 5} # ---> O tipo conjunto é utilizado para representar uma coleção de valores. Em Python, um conjunto não permite valores duplicados.
