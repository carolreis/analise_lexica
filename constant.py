# -*- coding: utf-8 -*-

'''
. = 46
0...9 = 48...57
'''

def constant(fita):
	index = 0
	tam = len(fita)

	# estado final
	def q5(fita, index):
		if index < tam:
			return False
		return 'float'

	# 0...9
	def q4(fita, index):
		if index < tam:
			if ord(fita[index]) >= 48 and ord(fita[index]) <= 57:
				index = index + 1
				return q5(fita, index)
			return False		
		return False

	# 0...9
	def q3(fita, index):
		if index < tam:
			if ord(fita[index]) >= 48 and ord(fita[index]) <= 57:
				index = index + 1
				return q4(fita, index)
			return False		
		return False

	# .
	def q2(fita, index):
		if index < tam:
			if ord(fita[index]) == 46:
				index = index + 1
				return q3(fita, index)
			return False
		return 'real'

	# 0...9
	def q1(fita, index):
		if index < tam:
			if ord(fita[index]) >= 48 and ord(fita[index]) <= 57:
				index = index + 1
				return q2(fita, index)
			return False
		# index igual ao tamanho = fim da fita
		return 'real'

	# 0...9
	def q0(fita, index):
		if index < tam:
			if ord(fita[index]) >= 48 and ord(fita[index]) <= 57:
				index = index + 1
				return q1(fita, index)
			return False
		return False

	return q0(fita, index)
