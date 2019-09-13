# -*- coding: utf-8 -*-

'''
--------------------------------------------------------
AUTÔMATO PARA RECONHECER PALAVRAS RESERVADAS
--------------------------------------------------------

----------------------------
CÓDIGO ASCII DOS CARACTERES
----------------------------
i 105 n 110 t 116
d 100 o 111 u 117 b 98 l 108 e 101
f 102 l 108 o 111 a 97 t 116
r 114 e 101 a 97 l 108
b 98 r 114 e 101 a 97 k 107
c 99 a 97 s 115 e 101
c 99 h 72 a 97 r 114
c 99 o 111 n 110 s 115 t 116
c 99 o 111 n 110 t 116 i 105 n 110 u 117 e 101
'''

def reserved(fita):
	index = 0
	tam = len(fita)

	def _char(fita, index):
		# estado final
		def q4(fita, index):
			if index < tam:
				return False
			return True

		def q3(fita, index):
			if index < tam:
				if (ord(fita[index]) == 114):
					index = index + 1
					return q4(fita, index)
				return False
			return False

		def q2(fita,index):
			if index < tam:
				if (ord(fita[index]) == 97):
					index = index + 1
					return q3(fita, index)
				return False
			return False

		def q1(fita, index):		
			if index < tam:
				if (ord(fita[index]) == 104):
					index = index + 1
					return q2(fita, index)
				return False
			return False

		def q0(fita, index):
			if index < tam:
				if (ord(fita[index]) == 99):
					index = index + 1
					return q1(fita, index)
				return False
			return False

		return q0(fita, index)

	def _int(fita, index):

		# estado final
		def q3(fita, index):
			if index < tam:
				return False
			return True

		def q2(fita,index):
			if index < tam:
				if (ord(fita[index]) == 116):
					index = index + 1
					return q3(fita, index)
				return False
			return False

		def q1(fita, index):		
			if index < tam:
				if (ord(fita[index]) == 110):
					index = index + 1
					return q2(fita, index)
				return False
			return False

		def q0(fita, index):
			if index < tam:
				if (ord(fita[index]) == 105):
					index = index + 1
					return q1(fita, index)
				return False
			return False

		return q0(fita, index)

	def _double(fita, index):
		# estado final
		def q6(fita, index):
			if index < tam:
				return False
			return True

		def q5(fita, index):
			if index < tam:
				if (ord(fita[index]) == 101):
					index = index + 1
					return q6(fita, index)
				return False
			return False

		def q4(fita, index):
			if index < tam:
				if (ord(fita[index]) == 108):
					index = index + 1
					return q5(fita, index)
				return False
			return False

		def q3(fita, index):
			if index < tam:
				if (ord(fita[index]) == 98):
					index = index + 1
					return q4(fita, index)
				return False
			return False

		def q2(fita,index):
			if index < tam:
				if (ord(fita[index]) == 117):
					index = index + 1
					return q3(fita, index)
				return False
			return False

		def q1(fita, index):		
			if index < tam:
				if (ord(fita[index]) == 111):
					index = index + 1
					return q2(fita, index)
				return False
			return False

		def q0(fita, index):
			if index < tam:
				if (ord(fita[index]) == 100):
					index = index + 1
					return q1(fita, index)
				return False
			return False

		return q0(fita, index)

	def _float(fita, index):
		# estado final
		def q5(fita, index):
			if index < tam:
				return False
			return True

		def q4(fita, index):
			if index < tam:
				if (ord(fita[index]) == 116):
					index = index + 1
					return q5(fita, index)
				return False
			return False

		def q3(fita, index):
			if index < tam:
				if (ord(fita[index]) == 97):
					index = index + 1
					return q4(fita, index)
				return False
			return False

		def q2(fita,index):
			if index < tam:
				if (ord(fita[index]) == 111):
					index = index + 1
					return q3(fita, index)
				return False
			return False

		def q1(fita, index):		
			if index < tam:
				if (ord(fita[index]) == 108):
					index = index + 1
					return q2(fita, index)
				return False
			return False

		def q0(fita, index):
			if index < tam:
				if (ord(fita[index]) == 102):
					index = index + 1
					return q1(fita, index)
				return False
			return False

		return q0(fita, index)

	def _real(fita, index):
		# estado final
		def q4(fita, index):
			if index < tam:
				return False
			return True

		def q3(fita, index):
			if index < tam:
				if (ord(fita[index]) == 108):
					index = index + 1
					return q4(fita, index)
				return False
			return False

		def q2(fita,index):
			if index < tam:
				if (ord(fita[index]) == 97):
					index = index + 1
					return q3(fita, index)
				return False
			return False

		def q1(fita, index):		
			if index < tam:
				if (ord(fita[index]) == 101):
					index = index + 1
					return q2(fita, index)
				return False
			return False

		def q0(fita, index):
			if index < tam:
				if (ord(fita[index]) == 114):
					index = index + 1
					return q1(fita, index)
				return False
			return False

		return q0(fita, index)
	
	def _break(fita, index):
		# estado final
		def q5(fita, index):
			if index < tam:
				return False
			return True

		def q4(fita, index):
			if index < tam:
				if (ord(fita[index]) == 107):
					index = index + 1
					return q5(fita, index)
				return False
			return False

		def q3(fita, index):
			if index < tam:
				if (ord(fita[index]) == 97):
					index = index + 1
					return q4(fita, index)
				return False
			return False

		def q2(fita,index):
			if index < tam:
				if (ord(fita[index]) == 101):
					index = index + 1
					return q3(fita, index)
				return False
			return False

		def q1(fita, index):		
			if index < tam:
				if (ord(fita[index]) == 114):
					index = index + 1
					return q2(fita, index)
				return False
			return False

		def q0(fita, index):
			if index < tam:
				if (ord(fita[index]) == 98):
					index = index + 1
					return q1(fita, index)
				return False
			return False

		return q0(fita, index)
	
	def _case(fita, index):
		# estado final
		def q4(fita, index):
			if index < tam:
				return False
			return True

		def q3(fita, index):
			if index < tam:
				if (ord(fita[index]) == 101):
					index = index + 1
					return q4(fita, index)
				return False
			return False

		def q2(fita,index):
			if index < tam:
				if (ord(fita[index]) == 115):
					index = index + 1
					return q3(fita, index)
				return False
			return False

		def q1(fita, index):		
			if index < tam:
				if (ord(fita[index]) == 97):
					index = index + 1
					return q2(fita, index)
				return False
			return False

		def q0(fita, index):
			if index < tam:
				if (ord(fita[index]) == 99):
					index = index + 1
					return q1(fita, index)
				return False
			return False

		return q0(fita, index)

	def _continue(fita, index):
		# estado final
		def q8(fita, index):
			if index < tam:
				return False
			return True

		def q7(fita, index):
			if index < tam:
				if (ord(fita[index]) == 101):
					index = index + 1
					return q8(fita, index)
				return False
			return False

		def q6(fita, index):
			if index < tam:
				if (ord(fita[index]) == 117):
					index = index + 1
					return q7(fita, index)
				return False
			return False

		def q5(fita, index):
			if index < tam:
				if (ord(fita[index]) == 110):
					index = index + 1
					return q6(fita, index)
				return False
			return False

		def q4(fita, index):
			if index < tam:
				if (ord(fita[index]) == 105):
					index = index + 1
					return q5(fita, index)
				return False
			return False

		def q3(fita, index):
			if index < tam:
				if (ord(fita[index]) == 116):
					index = index + 1
					return q4(fita, index)
				return False
			return False

		def q2(fita,index):
			if index < tam:
				if (ord(fita[index]) == 110):
					index = index + 1
					return q3(fita, index)
				return False
			return False

		def q1(fita, index):		
			if index < tam:
				if (ord(fita[index]) == 111):
					index = index + 1
					return q2(fita, index)
				return False
			return False

		def q0(fita, index):
			if index < tam:
				if (ord(fita[index]) == 99):
					index = index + 1
					return q1(fita, index)
				return False
			return False

		return q0(fita, index)

	def _const(fita, index):
		# estado final
		def q5(fita, index):
			if index < tam:
				return False
			return True

		def q4(fita, index):
			if index < tam:
				if (ord(fita[index]) == 116):
					index = index + 1
					return q5(fita, index)
				return False
			return False

		def q3(fita, index):
			if index < tam:
				if (ord(fita[index]) == 115):
					index = index + 1
					return q4(fita, index)
				return False
			return False

		def q2(fita,index):
			if index < tam:
				if (ord(fita[index]) == 110):
					index = index + 1
					return q3(fita, index)
				return False
			return False

		def q1(fita, index):		
			if index < tam:
				if (ord(fita[index]) == 111):
					index = index + 1
					return q2(fita, index)
				return False
			return False

		def q0(fita, index):
			if index < tam:
				if (ord(fita[index]) == 99):
					index = index + 1
					return q1(fita, index)
				return False
			return False

		return q0(fita, index)

	# Retorna o tipo reconhecido
	if _int(fita, index):
		return 'int'
	elif _double(fita, index):
		return 'double'
	elif _float(fita, index):
		return 'float'
	elif _real(fita, index):
		return 'real'
	elif _break(fita, index):
		return 'break'
	elif _case(fita, index):
		return 'case'
	elif _char(fita, index):
		return 'char'
	elif _continue(fita, index):
		return 'continue'
	elif _const(fita, index):
		return 'const'
	else:
		return False
