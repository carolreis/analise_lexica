# -*- coding: utf-8 -*-

'''
--------------------------------------------------------
AUTÔMATO PARA RECONHECER CONSNTANTES (INTEIRO / REAL)
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
		Neste caso, o número é REAL
	'''
	def q5(fita, index):
		if index < tam:
			return False
		return 'número real'

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
		Neste caso, o número é INTEIRO
		Se não for, reconhece o "."
	'''
	def q2(fita, index):
		if index < tam:
			if ord(fita[index]) == 46:
				index = index + 1
				return q3(fita, index)
			return False
		return 'número inteiro'

	'''
		ESTADO FINAL
		Neste caso, o número é INTEIRO
		Reconhece X{0...9}
	'''
	def q1(fita, index):
		if index < tam:
			if ord(fita[index]) >= 48 and ord(fita[index]) <= 57:
				index = index + 1
				return q2(fita, index)
			return False
		return 'número inteiro'

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
