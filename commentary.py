# -*- coding: utf-8 -*-

'''
--------------------------------------------------------
AUTÔMATO PARA RECONHECER COMENTÁRIOS
--------------------------------------------------------

----------------------------
CÓDIGO ASCII DOS CARACTERES
----------------------------
/ = 47
'''

def commentary(fita):
	index = 0
	tam = len(fita)

	def q2(fita, index):
		while index < tam:
			if ord(fita[index]) != 92:
				index = index + 1
			else:
				return False
		return True

	def q1(fita, index):		
		if index < tam:
			if ord(fita[index]) == 47:
				index = index + 1
				return q2(fita, index)
			return False
		return False

	def q0(fita, index):
		if index < tam:
			if ord(fita[index]) == 47:
				index = index + 1
				return q1(fita, index)
			return False
		return False

	return q0(fita, index)
