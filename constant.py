# -*- coding: utf-8 -*-

'''
--------------------------------------------------------
AUTÔMATO PARA RECONHECER CONSNTANTES (REAL / FLOAT)
--------------------------------------------------------

----------------------------
CÓDIGO ASCII DOS CARACTERES
----------------------------
. = 46
0...9 = 48...57
'''

def constant(fita):
	index = 0
	tam = len(fita)

	'''
		ESTADO FINAL
		Neste caso, o número é FLOAT
	'''
	def q5(fita, index):
		if index < tam:
			return False
		return 'float'

	'''
		Reconhece XX.X{0...9}
	'''
	def q4(fita, index):
		if index < tam:
			if ord(fita[index]) >= 48 and ord(fita[index]) <= 57:
				index = index + 1
				return q5(fita, index)
			return False		
		return False

	'''
		Reconhece XX.{0...9}X
	'''
	def q3(fita, index):
		if index < tam:
			if ord(fita[index]) >= 48 and ord(fita[index]) <= 57:
				index = index + 1
				return q4(fita, index)
			return False		
		return False

	'''
		ESTADO FINAL
		Neste caso, o número é REAL
		Se não for, reconhece o "."
	'''
	def q2(fita, index):
		if index < tam:
			if ord(fita[index]) == 46:
				index = index + 1
				return q3(fita, index)
			return False
		return 'real'

	'''
		ESTADO FINAL
		Neste caso, o número é REAL
		Reconhece X{0...9}
	'''
	def q1(fita, index):
		if index < tam:
			if ord(fita[index]) >= 48 and ord(fita[index]) <= 57:
				index = index + 1
				return q2(fita, index)
			return False
		return 'real'

	'''
		Reconhece {0...9}
	'''
	def q0(fita, index):
		if index < tam:
			if ord(fita[index]) >= 48 and ord(fita[index]) <= 57:
				index = index + 1
				return q1(fita, index)
			return False
		return False

	return q0(fita, index)
