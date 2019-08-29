# -*- coding: utf-8 -*-
from identifier import *
from constant import *
from commentary import *
from reserved import *

map_tokens = []
table_symbols = []

# Identifier 
fita_identifier = "t"
# print(fita_identifier)
# print identifier(fita_identifier)

# Constantes
fita_constantes = '99.99'
# print(fita_constantes)
# print constant(fita_constantes)

# Comentários
fita_comentario = '//'
# print(fita_comentario)
# print commentary(fita_comentario)

# Palavras reservadas
fita_reservada = 'double'
# print reserved(fita_reservada)

'''
==============================================
'''

fita = ''

if reserved(fita):
	print 'reservada'
elif identifier(fita):
	print 'identificador'
elif constant(fita):
	print 'constante'
elif commentary(fita):
	print 'comentário'
else:
	print 'não reconhecido'

# print(table_symbols)
# print(map_tokens)
