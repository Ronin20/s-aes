# coding: utf-8

sbox = [['9', '4', 'A', 'B'], ['D', '1', '8', '5'], ['6', '2', '0', '3'], ['C', 'E', 'F', '7']]
sboxInverse = [['A', '5', '9', 'B'], ['1', '7', '8', 'F'], ['6', '0', '2', '3'], ['C', '4', 'D', 'E']]

addTable = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'],
			['1', '0', '3', '2', '5', '4', '7', '6', '9', '8', 'B', 'A', 'D', 'C', 'F', 'E'],
			['2', '3', '0', '1', '6', '7', '4', '5', 'A', 'B', '8', '9', 'E', 'F', 'C', 'D'],
			['3', '2', '1', '0', '7', '6', '5', '4', 'B', 'A', '9', '8', 'F', 'E', 'D', 'C'],
			['4', '5', '6', '7', '0', '1', '2', '3', 'C', 'D', 'E', 'F', '8', '9', 'A', 'B'],
			['5', '4', '7', '6', '1', '0', '3', '2', 'D', 'C', 'F', 'E', '9', '8', 'B', 'A'],
			['6', '7', '4', '5', '2', '3', '0', '1', 'E', 'F', 'C', 'D', 'A', 'B', '8', '9'],
			['7', '6', '5', '4', '3', '2', '1', '0', 'F', 'E', 'D', 'C', 'B', 'A', '9', '8'],
			['8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7'],
			['9', '8', 'B', 'A', 'D', 'C', 'F', 'E', '1', '0', '3', '2', '5', '4', '7', '6'],
			['A', 'B', '8', '9', 'E', 'F', 'C', 'D', '2', '3', '0', '1', '6', '7', '4', '5'],
			['B', 'A', '9', '8', 'F', 'E', 'D', 'C', '3', '2', '1', '0', '7', '6', '5', '4'],
			['C', 'D', 'E', 'F', '8', '9', 'A', 'B', '4', '5', '6', '7', '0', '1', '2', '3'],
			['D', 'C', 'F', 'E', '9', '8', 'B', 'A', '5', '4', '7', '6', '1', '0', '3', '2'],
			['E', 'F', 'C', 'D', 'A', 'B', '8', '9', '6', '7', '4', '5', '2', '3', '0', '1'],
			['F', 'E', 'D', 'C', 'B', 'A', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
]

multTable = [
			['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
			['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'],
			['0', '2', '4', '6', '8', 'A', 'C', 'E', '3', '1', '7', '5', 'B', '9', 'F', 'D'],
			['0', '3', '6', '5', 'C', 'F', 'A', '9', 'B', '8', 'D', 'E', '7', '4', '1', '2'],
			['0', '4', '8', 'C', '3', '7', 'B', 'F', '6', '2', 'E', 'A', '5', '1', 'D', '9'],
			['0', '5', 'A', 'F', '7', '2', 'D', '8', 'E', 'B', '4', '1', '9', 'C', '3', '6'],
			['0', '6', 'C', 'A', 'B', 'D', '7', '1', '5', '3', '9', 'F', 'E', '8', '2', '4'],
			['0', '7', 'E', '9', 'F', '8', '1', '6', 'D', 'A', '3', '4', '2', '5', 'C', 'B'],
			['0', '8', '3', 'B', '6', 'E', '5', 'D', 'C', '4', 'F', '7', 'A', '2', '9', '1'],
			['0', '9', '1', '8', '2', 'B', '3', 'A', '4', 'D', '5', 'C', '6', 'F', '7', 'E'],
			['0', 'A', '7', 'D', 'E', '4', '9', '3', 'F', '5', '8', '2', '1', 'B', '6', 'C'],
			['0', 'B', '5', 'E', 'A', '1', 'F', '4', '7', 'C', '2', '9', 'D', '6', '8', '3'],
			['0', 'C', 'B', '7', '5', '9', 'E', '2', 'A', '6', '1', 'D', 'F', '3', '4', '8'],
			['0', 'D', '9', '4', '1', 'C', '8', '5', '2', 'F', 'B', '6', '3', 'E', 'A', '7'],
			['0', 'E', 'F', '1', 'D', '3', '2', 'C', '9', '7', '6', '8', '4', 'A', 'B', '5'],
			['0', 'F', 'D', '2', '9', '6', '4', 'B', '1', 'E', 'C', '3', '8', '7', '5', 'A']
]


#----------------------------Funções de conversão------------------------------

def stringToHex(par): # Converte um par de simbolos para Hexadecimal
	new = ''	
	new += par[0].encode("utf-8").hex()
	new += par[1].encode("utf-8").hex()
	return new

def hexToBinary(hex): # Converte Hexadecimal para binário
    b = int(hex, 16)
    binary = bin(b)
    binary = binary[2:]
    return '{:0>4}'.format(binary) # Sempre retorna 4 digitos


#--------------------------- Operações -----------------------------

def xorGeral(a, b): # Faz o xor entre dois valores hexadecimais
	result = int(a, 16) ^ int(b, 16) # Converte para inteiro e faz o xor entre eles
	return '{:0>4x}'.format(result)  # Converte de vola para hexadecimal, sempre com 4 digitos


def concatenaMatriz(mat): # Concatena a matriz em uma string
	concatena = ''
	for i in mat:
		for j in i:
			concatena += j
	return concatena

def geraMatriz(simbols): # Recebe dois simbolos e gera a matriz Estado
	mat = [['', ''], ['', '']]
	msghex = stringToHex(simbols)
	mat[0][0] = msghex[0]
	mat[0][1] = msghex[1]
	mat[1][0] = msghex[2]
	mat[1][1] = msghex[3]
	return mat

#------------------------ Funções auxiliares ----------------------
def rotWord(w):
	return w[1:] + w[0]

def search(table, l, c):
	l = int(l, 16)
	c = int(c, 16)
	return table[l][c]

def sub(par):
	new_par = ''
	for j in range(2): 
		elemento = par[j] # Guarda o elemento
		elemento = hexToBinary(elemento) # Converte para hexa decimal
		l = elemento[:2] # Pega os dois primeiros digitos que serão a linha
		c = elemento[2:] # Pega os dois ultimos digitos que serão a coluna
		l = int(l, 2) # Converte para binário
		c = int(c, 2)
		new_par += sbox[l][c]
	return new_par



#------------------------ Métodos ----------------------

def embaralharColunas(mat):
	new_mat = [['', ''], ['', '']]
	new_mat[0][0] = search(addTable, mat[0][0], search(multTable, '4', mat[1][0]))
	new_mat[0][1] = search(addTable, search(multTable, '4', mat[0][0]), mat[1][0])
	new_mat[1][0] = search(addTable, mat[0][1], search(multTable, '4', mat[1][1]))
	new_mat[1][1] = search(addTable, search(multTable, '4', mat[0][1]), mat[1][1])
	return new_mat

def incluirChave(mat, chave): 
	a = concatenaMatriz(mat) # Concatena a matriz de estado
	b = concatenaMatriz(chave) # Concatena a matriz da chave
	xor = xorGeral(a, b) # Faz o xor entre as duas matrizes
	ind = 0
	for i in range(2): # Coloca tudo em uma matriz de novo e retorna
		for j in range(2):
			mat[i][j] = xor[ind]
			ind += 1
	return mat

def subNibble(mat): # Faz a substituição dos Nibbles
	for i in range(2): # Percorre a matriz inteira analisando cada simbolo
		for j in range(2): 
			elemento = mat[i][j] # Guarda o elemento
			elemento = hexToBinary(elemento) # Converte para hexa decimal
			l = elemento[:2] # Pega os dois primeiros digitos que serão a linha
			c = elemento[2:] # Pega os dois ultimos digitos que serão a coluna
			l = int(l, 2) # Converte para binário
			c = int(c, 2)
			mat[i][j] = sbox[l][c] # Busca na sbox e atualiza o elemento
	return mat

def deslocarLinhas(mat):
	mat[1][0], mat[1][1] = mat[1][1], mat[1][0] # Apenas troca os elementos da segunda linha
	return mat


#chave = [['2', '5'], ['D', '5']]




def keySchedule(key):
	ws = list()
	tmp = list()
	for i in key: #Pega a chave em hexadecimal e coloca tudo em binario pra formar a matriz 4x4
		for j in i:
			tmp.append(hexToBinary(j))
			ws.append(tmp[:])
			tmp.clear()
	
	for i in range(4):
		pass



	print(ws)

#matrizEstado = [['A', '4'], ['7', '9']]
#chave = [['2', '5'], ['D', '5']]


#---------------------- Funções principais --------------------

def encrypt():
	matrizEstado = list()
	matrizChave = list()
	'''
	text_plain = input('Digite o texto claro: ')
	key = input('Digite a chave de encriptação: ')

	text_plain = text_plain[:2] # Reduz o texto claro a apenas os dois primeiros simbolos
	key = key[:2] # Reduz a chave a apenas os dois primeiros simbolos

	matrizEstado = geraMatriz(text_plain)
	matrizChave = geraMatriz(key)
	'''
	matrizEstado = [['A', '4'], ['7', '9']]
	matrizChave = [['2', '5'], ['D', '5']]
	'''
	matrizEstado = incluirChave(matrizEstado, matrizChave)
	


	matrizEstado = subNibble(matrizEstado)
	matrizEstado = deslocarLinhas(matrizEstado)
	matrizEstado = embaralharColunas(matrizEstado)
	



	print(matrizEstado)
'''
	keySchedule(matrizChave)	
	print('Antes: ', matrizChave, 'Depois: ', rotWord(matrizChave))



encrypt()
