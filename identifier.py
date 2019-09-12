# -*- coding: utf-8 -*-

'''
--------------------------------------------------------
AUTÔMATO PARA RECONHECER IDENTIFICADORES
--------------------------------------------------------

----------------------------
CÓDIGO ASCII DOS CARACTERES
----------------------------
A...Z = 65...90
a...z = 97...112
0...9 = 48...57
_ = 95
'''

def identifier(fita):
	index = 0
	tam = len(fita)

	'''
		ESTADO Q1
		Loop enquanto os caracteres forem = {A-Z|a-z|0-9|_}
	'''
	def q1(fita, index):		
		while index < tam:
			if (
				(ord(fita[index]) >= 65 and ord(fita[index]) <= 90) 
				or (ord(fita[index]) >= 97 and ord(fita[index]) <= 122)
				or (ord(fita[index]) >= 48 and ord(fita[index]) <= 57)
				or ord(fita[index]) == 95
			):
				index = index + 1
			else:
				return False
		return True

	'''
	ESTADO INICIAL
	Verifica se inicia com letras ou _
	'''
	def q0(fita, index):
		if index < tam:
			if (ord(fita[index]) >= 65 and ord(fita[index]) <= 90) or (ord(fita[index]) >= 97 and ord(fita[index]) <= 122) or ord(fita[index]) == 95:
				index = index + 1
				return q1(fita, index)
			return False
		return False

	return q0(fita, index)