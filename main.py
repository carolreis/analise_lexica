# -*- coding: utf-8 -*-
import sys
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
Tabela de Tokens:
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

# Lê nome de arquivo da linha de comando
if len(sys.argv) > 1:
	arquivo = sys.argv[1] 
else:
	arquivo = 'teste2.txt'

with open(arquivo) as f:

	for fita in f:

		fita = fita.strip('\r\n')

		# Cria novo registro de token
		token = {}

		# Executa os autômatos e retorna o tipo ou False
		r = reserved(fita)
		i = identifier(fita)
		con = constant(fita)
		com = commentary(fita)

		''' 
			Busca identificador / constante na tabela de símbolos
			para verificar se a palavra já foi adicionada anteriormente
		'''
		find_type = filter(lambda simbolo: simbolo['valor'] == fita, tabela_simbolos)

		# Palavra reservada
		if r:
			# Adiciona dados do token
			token = {
				'linha': linha,
				'tipo': r,
				'id': ""
			}
			# Adiciona registro na tabela de token
			tokens.append(token)
		# Identificador
		elif i:
			# Adiciona dados do token
			token = {
				'linha': linha,
				'tipo': 'identificador',
				'id': _id if not find_type else find_type[0]['id']
			}
			# Adiciona registro na tabela de token
			tokens.append(token)

			'''
				Se o registro não foi adicionado anteriormente, incrementa o ID e adiciona na tabela de símbolos
			''' 
			if not find_type:
				tabela_simbolos.append({"id": _id, "valor":fita})
				_id = _id + 1
		# Constante
		elif con:
			# Adiciona dados do token
			token = {
				'linha': linha, 
				'tipo': con,
				'id': _id if not find_type else find_type[0]['id']
			}
			# Adiciona registro na tabela de token
			tokens.append(token)

			'''
				Se o registro não foi adicionado anteriormente, incrementa o ID e adiciona na tabela de símbolos
			''' 
			if not find_type:
				tabela_simbolos.append({"id": _id, "valor":fita})
				_id = _id + 1
		# Comentario
		elif com:
			# Adiciona dados do token
			token = {
				'linha': linha, 
				'tipo': 'comentário',
				'id': ''
			}
			# Adiciona na tabela de token
			tokens.append(token)
		else:
			# Nao reconhecido = erro
			erros.append({'linha':linha})
	
		linha = linha + 1

# Imprime os tokens
for token in tokens:
	print "[%d] %s %s" % (token['linha'], token['tipo'], token['id'])

print "\nTabela de símbolos:"
# Imprime a tabela de símbolos
for simbolo in tabela_simbolos:
	print "%d - %s" % (simbolo['id'], simbolo['valor'])

# Exibe os erros
print "\nO programa possui erro nas linhas:"
for erro in erros:
	print erro['linha']
