# -*- coding: utf-8 -*-
from identifier import *
from constant import *
from commentary import *
from reserved import *

tokens = {}
symbol_table = {}
errors = {}
line = 1
_id = 1

#loop
fita = ''
token = {}

r = reserved(fita)
i = identifier(fita)
con = constant(fita)
com = commentary(fita)

if r:
	token = {
		'linha': line,
		'tipo': r
	}
	tokens.update(token)
elif i:
	token = {
		'linha': line,
		'tipo': 'identificador',
		'id': _id
	}
	tokens.update(token)
	symbol_table.update({_id:fita})
elif con:
	token = {
		'linha': line, 
		'tipo': 'constante',
		'id': _id
	}
	tokens.update(token)
	symbol_table.update({_id:fita})
elif com:
	token = {
		'linha': line, 
		'tipo': 'comentário',
		'id': _id
	}
	tokens.update(token)
else:
	print 'não reconhecido'
	errors.update({'line':line})

print(tokens)
print(symbol_table)
print(errors)

'''
Verificar se já existe o identificador

'''

'''
Quando der erro não exibe
Mas contabiliza a linha
'''