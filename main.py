# -*- coding: utf-8 -*-
from identifier import *
from constant import *
from commentary import *
from reserved import *

tokens = []
tabela_simbolos = []
erros = []
linha = 1
_id = 1

'''
Tokens:
[
	{
	linha: NUMERO DA LINHA,
	tipo: 'identificador' / 'constante' / ...,
	id: ID
	}
]
'''

'''
Tabela de símbolos: (para números e identificadores)

[
	{
	id: ID,
	valor: 'VALOR LIDO NA FITA'
	},
	...
]

'''

arquivo = 'teste.txt'

with open(arquivo) as f:

	for fita in f:

		fita = fita.strip('\n')

		token = {}

		r = reserved(fita)
		i = identifier(fita)
		con = constant(fita)
		com = commentary(fita)

		# Busca identificador / constante na tabela de símbolos
		find_type = filter(lambda simbolo: simbolo['valor'] == fita, tabela_simbolos)

		# Palavra reservada
		if r:
			token = {
				'linha': linha,
				'tipo': r,
				'id': ""
			}
			tokens.append(token)
		# Identificador
		elif i:
			token = {
				'linha': linha,
				'tipo': 'identificador',
				'id': _id if not find_type else find_type[0]['id']
			}
			tokens.append(token)
			if not find_type:
				tabela_simbolos.append({"id": _id, "valor":fita})
				_id = _id + 1
		# Constante
		elif con:
			token = {
				'linha': linha, 
				'tipo': con,
				'id': _id if not find_type else find_type[0]['id']
			}
			tokens.append(token)
			if not find_type:
				tabela_simbolos.append({"id": _id, "valor":fita})
				_id = _id + 1
		# Comentario
		elif com:
			token = {
				'linha': linha, 
				'tipo': 'comentário',
				'id': ''
			}
			tokens.append(token)
		# Nao reconhecido = erro
		else:
			erros.append({'linha':linha})
	
		linha = linha + 1

for token in tokens:
	print "[%d] %s %s" % (token['linha'], token['tipo'], token['id'])

print "\nTabela de símbolos:"

for simbolo in tabela_simbolos:
	print "%d - %s" % (simbolo['id'], simbolo['valor'])

print "\nO programa possui erro nas linhas:"
for erro in erros:
	print erro['linha'] # VAI VIRAR UM ARRAY
