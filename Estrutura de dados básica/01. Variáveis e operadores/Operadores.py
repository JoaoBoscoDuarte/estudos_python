"""
Em Python, existem os seguintes operadores:
    Aritméticos
    Relacionais
    Lógicos
    Atribuição
    Identidade
    Membro
    Bitwise
"""


#Aritimeticos (Os operadores aritméticos são utilizados para realizar operações aritméticas.)
soma = 10 + 5
subtracao = 10 - 5
multiplicacao = 10 * 5
divisao = 10 / 5
modulo = 10 % 5
divisaoInteira = 10 //5
exponenciacao = 10 ** 5


#Comparação
menor = 10 < 5 #>>>false
maior = 10 > 5 #>>>true
menorigual = 10 <= 10 #>>>true
maiorigual = 10 >= 10 #>>>true
diferente = 10 != 5 #>>>true


#Relacionais (Os operadores relacionais são utilizados para realizar comparações entre valores.)
igual = (5 == 5)
diferente = (5 != 5)


#Lógicos (Os operadores lógicos são utilizados para realizar operações lógicas.);
e = 10 and 5 #dez e cinco (equivalente a &&);
ou = 10 or 5 #dez ou cinco (equivalente a ||);
nao = not 5 #não, inverso da verdade (equivalente a !);


#Atribuição (atribui x a y);
atribucao = 2 #Saída: 2
atribucao += 2 #Saída: 4
atribucao -= 1 #Saída: 3
atribucao *= 2 #Saída: 6


#Identidade (Os operadores de identidade são utilizados para verificar se duas variáveis são iguais ou diferentes.);
x = 1
y = 2


igual = x is y #x é igual a y
eDiferente = x is not y #x não é y


#menbro (Os operadores de membro são utilizados para verificar se um valor pertence a uma coleção.);
pertence = x in y #x pertence a y
naoPertence = x not in y #x não pertence a y


#bitwise (Os operadores bitwise são utilizados para realizar operações bitwise)
"""
______________________________________________________________________
Operador	Descrição	                Exemplo
&	        AND	                        10 & 5
|	        OR	                        10 | 5
^	        XOR	                         10 ^ 5
~	        NOT	                        ~10
<<	        Deslocamento à esquerda	    10 << 5
>>	        Deslocamento à direita	    10 >> 5
------------------------------------------------------------------------
"""
