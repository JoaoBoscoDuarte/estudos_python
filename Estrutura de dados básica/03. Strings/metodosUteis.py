#Maiúscula, minúscula e títulos
name = 'QuaLQuer CoISa'

print(name.upper()) #>> QUALQUER COISA
print(name.lower()) #>> qualquer coisa
print(name.title()) #>> Qualquer Coisa

#Eliminar os espaços da string
name = '   Curso  '

print(name.strip()) #>>'Curso'
print(name.lstrip()) #>>'Curso  '
print(name.rstrip()) #>> '   Curso'

#Junções e centralizações
variavel = 'Boscola'

print(variavel.center(11, '#')) #>> '##Boscola##'
print('.'.join(variavel)) #>> 'B.o.s.c.o.l.a'