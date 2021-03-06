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

#--------------------------- Funções de conversão -----------------------------

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

def binToHex(b):
	result = hex(int(b, 2))
	return result[2:]

def decToBin(d):
	return '{:0>4}' .format(str(bin(d))[2:])

def hexToString(h):
	return bytearray.fromhex(h).decode()
#--------------------------- Operações -----------------------------

def xorGeral(a, b): # Faz o xor entre dois valores hexadecimais
	result = int(a, 16) ^ int(b, 16) # Converte para inteiro e faz o xor entre eles
	return '{:0>4x}'.format(result)  # Converte de vola para hexadecimal, sempre com 4 digitos

def xorBinary(a, b):
	result = int(a,2) ^ int(b,2)
	result = bin(result)
	return '{:0>4}'.format(result[2:])

def concatenaMatriz(mat): # Concatena a matriz em uma string
	concatena = ''
	for i in mat:
		for j in i:
			concatena += str(j)
	return concatena

def geraMatriz(simbols): # Recebe dois simbolos e gera a matriz Estado
	mat = [['', ''], ['', '']]
	msghex = stringToHex(simbols)
	mat[0][0] = msghex[0]
	mat[1][0] = msghex[1] #Alterei o formato aqui, rever isso depois
	mat[0][1] = msghex[2]
	mat[1][1] = msghex[3]
	return mat

def montaMatriz(simbols): 
	mat = [['', ''], ['', '']]
	mat[0][0] = simbols[0]
	mat[0][1] = simbols[1] 
	mat[1][0] = simbols[2]
	mat[1][1] = simbols[3]
	return mat

def separa(lista):
	processada = list()
	tmp = list()
	if len(lista) % 2:
		lista += '0'
	for i in range(0,len(lista),2):
		tmp.append(lista[i])
		tmp.append(lista[i+1])
		processada.append(tmp[:])
		tmp.clear()
	return processada

#------------------------ Funções auxiliares ----------------------
def rotWord(w):
	return w[1:] + w[0]

def search(table, l, c):
	l = int(l, 16)
	c = int(c, 16)
	return table[l][c]

def sub(par):
	l = par[:2] # Pega os dois primeiros digitos que serão a linha
	c = par[2:] # Pega os dois ultimos digitos que serão a coluna
	l = int(l, 2) # Converte para decimal
	c = int(c, 2)
	return hexToBinary(sbox[l][c])

#------------------------ Métodos ----------------------

def mixColumns(mat):
	new_mat = [['', ''], ['', '']]
	new_mat[0][0] = search(addTable, mat[0][0], search(multTable, '4', mat[1][0]))
	new_mat[1][0] = search(addTable, search(multTable, '4', mat[0][0]), mat[1][0])
	new_mat[0][1] = search(addTable, mat[0][1], search(multTable, '4', mat[1][1]))
	new_mat[1][1] = search(addTable, search(multTable, '4', mat[0][1]), mat[1][1])
	return new_mat

def mixColumnsInverse(mat):
	new_mat = [['', ''], ['', '']]
	new_mat[0][0] = search(addTable, search(multTable, '2', mat[0][0]), search(multTable, '9', mat[1][0]))
	new_mat[1][0] = search(addTable, search(multTable, '9', mat[0][0]), search(multTable, '2', mat[1][0]))
	new_mat[0][1] = search(addTable, search(multTable, '2', mat[0][1]), search(multTable, '9', mat[1][1]))
	new_mat[1][1] = search(addTable, search(multTable, '9', mat[0][1]), search(multTable, '2', mat[1][1]))
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

def subBytes(mat, box): # Faz a substituição dos Nibbles
	for i in range(2): # Percorre a matriz inteira analisando cada simbolo
		for j in range(2): 
			elemento = mat[i][j] # Guarda o elemento
			elemento = hexToBinary(elemento) # Converte para hexa decimal
			l = elemento[:2] # Pega os dois primeiros digitos que serão a linha
			c = elemento[2:] # Pega os dois ultimos digitos que serão a coluna
			l = int(l, 2) # Converte para binário
			c = int(c, 2)
			mat[i][j] = box[l][c] # Busca na sbox e atualiza o elemento
	return mat

def shiftRows(mat):
	mat[1][0], mat[1][1] = mat[1][1], mat[1][0] # Apenas troca os elementos da segunda linha
	return mat

def keySchedule(key, rcon):
	ws = list()
	tmp = list()
	new_key = ''
	for i in key:
		for j in i:
			tmp.append(hexToBinary(j))
			ws.append(tmp[:])
			tmp.clear()
	rot = rotWord(''.join(ws[3])) #Rotaciona
	par = sub(rot) # Substitui na sbox
	first_xor = xorBinary(''.join(ws[0]), par)
	second_xor = xorBinary(first_xor, rcon)
	tmp.append(second_xor)
	ws.append(tmp[:])
	tmp.clear()
	for i in range(1, 4):
		tmp.append(xorBinary(''.join(ws[i]), ''.join(ws[i+3]))) #Faz um xor
		ws.append(tmp[:])
		tmp.clear()	
	#print(ws[4:])
	for i in ws[4:]:
		for j in i:
			new_key += binToHex(j) #Converte pra hexa
	print('Key of this round: {}'.format(new_key))
	return new_key

def generateKeys(chave, round):
	lista_chaves = list()
	for i in range(0, round):
		chave = keySchedule(chave, decToBin(2**i))
		lista_chaves.append(chave)
		chave = montaMatriz(chave)
	return lista_chaves

def addRoundKey(mat, chave, rcon):
	new_mat = [['', ''], ['', '']]
	
	new_key = keySchedule(chave, rcon)
	new_mat = xorGeral(concatenaMatriz(mat), new_key)
	
	mat[0][0] = new_mat[0]
	mat[0][1] = new_mat[1] 
	mat[1][0] = new_mat[2]
	mat[1][1] = new_mat[3]
	return mat, montaMatriz(new_key)

#---------------------- Métodos principais --------------------

def encrypt(text_plain, key, rounds):
	cifrada = ''
	#cif = '0000'
	text_plain = text_plain.upper()
	text_plain = separa(text_plain)	

	for par in text_plain:
		matrizEstado = geraMatriz(par)
		print('matrizEstado: {}'.format(matrizEstado))
		matrizChave = geraMatriz(key)
		print('matrizChave: {}'.format(matrizChave))		
		matrizEstado = incluirChave(matrizEstado, matrizChave)
		print('Incluindo chave na matriz...')
		print('matrizEstado: {}'.format(matrizEstado))
		print('Começando a rodar...')
		for i in range(0, rounds):
			print('Round {}'.format(i))
			matrizEstado = subBytes(matrizEstado, sbox)
			print('1 - subBytes: {}'.format(matrizEstado))
			matrizEstado = shiftRows(matrizEstado)
			print('2 - shiftRows: {}'.format(matrizEstado))
			matrizEstado = mixColumns(matrizEstado)
			print('3 - mixColumns: {}'.format(matrizEstado))
			matrizEstado, matrizChave = addRoundKey(matrizEstado, matrizChave,  decToBin(2**i))
			print('4 - addRoundKey: {}'.format(matrizEstado))
		cif = concatenaMatriz(matrizEstado)
		cifrada += cif
	return cifrada


def decrypt(text, key, rounds):
	text_plain = ''
	matrizChave = geraMatriz(key)
	chaves = generateKeys(matrizChave, rounds)
	chaves = chaves[::-1]
	print('chaves: ', chaves)
	
	inicio = 0
	fim = 4
	
	for p in range(int(len(text)/4)):
		parte = text[inicio : fim]
		inicio = fim
		fim += 4
		matrizEstado = montaMatriz(parte)
		for i in range(rounds):
			matrizEstado =  montaMatriz(xorGeral(concatenaMatriz(matrizEstado), chaves[i]))
			#print('Adicionando a chave; {}'.format(matrizEstado))
			matrizEstado = mixColumnsInverse(matrizEstado)
			matrizEstado[0], matrizEstado[1] = matrizEstado[1], matrizEstado[0]
			#print('Mix Columns inverse: {}'.format(matrizEstado))
			matrizEstado = shiftRows(matrizEstado)
			#print(matrizEstado)
			matrizEstado = subBytes(matrizEstado, sboxInverse)
			#print(matrizEstado)
		matrizEstado = montaMatriz(xorGeral(concatenaMatriz(matrizEstado), concatenaMatriz(matrizChave)))
		matrizEstado[0][1], matrizEstado[1][0] = matrizEstado[1][0], matrizEstado[0][1]
		rodada = concatenaMatriz(matrizEstado)
		rodada = hexToString(rodada)
		text_plain += rodada
	return text_plain


def encrypt_cbc(text_plain, key, rounds):
	cifrada = ''
	cif = '0000'
	text_plain = text_plain.upper()
	text_plain = separa(text_plain)	

	for par in text_plain:
		matrizEstado = geraMatriz(par)
		print('ANTES: ', matrizEstado)

		matrizEstado = concatenaMatriz(matrizEstado)
		matrizEstado = xorGeral(matrizEstado, cif)
		matrizEstado = montaMatriz(matrizEstado)
		print('DEPOIS: ', matrizEstado)
		
		print('matrizEstado: {}'.format(matrizEstado))
		matrizChave = geraMatriz(key)
		print('matrizChave: {}'.format(matrizChave))		
		matrizEstado = incluirChave(matrizEstado, matrizChave)
		print('Incluindo chave na matriz...')
		print('matrizEstado: {}'.format(matrizEstado))
		print('Começando a rodar...')
		for i in range(0, rounds):
			print('Round {}'.format(i))
			matrizEstado = subBytes(matrizEstado, sbox)
			print('1 - subBytes: {}'.format(matrizEstado))
			matrizEstado = shiftRows(matrizEstado)
			print('2 - shiftRows: {}'.format(matrizEstado))
			matrizEstado = mixColumns(matrizEstado)
			print('3 - mixColumns: {}'.format(matrizEstado))
			matrizEstado, matrizChave = addRoundKey(matrizEstado, matrizChave,  decToBin(2**i))
			print('4 - addRoundKey: {}'.format(matrizEstado))
		cif = concatenaMatriz(matrizEstado)
		cifrada += cif
	return cifrada

#---------------------- Função principal --------------------

def main ():
	matrizEstado = list()
	matrizChave = list()
	while True:
		text = input('Digite o texto: ')
		key = input('Digite a chave de encriptação: ').upper()[:2]
		while True:
			rounds = int(input('Quantidade de rounds [1 - 4]: '))
			if 0 < rounds < 5:
				break
			else:
				print('Quantidade inválida, ', end='')

		print('1 - S-Aes ECB')
		print('2 - S-Aes CBC')
		print('3 - S-Aes CTR')
		print('4 - Sair')
		resp = int(input('Escolha uma opção: '))
		if resp == 1:	
			print('1 - Criptografar')
			print('2 - Descriptografar')
			while True:
				resp = int(input('Escolha uma opção: '))
				if resp == 1:		
					print('Result: >>>>>>>>> {} <<<<<<<<<'.format(encrypt(text, key, rounds)))
					break
				elif resp == 2:
					print('Result: >>>>>>>>> {} <<<<<<<<<'.format(decrypt(text, key, rounds)))
					break
				else:
					print('Opção inválida, ', end='')
		elif resp == 2:
			print('1 - Criptografar')
			print('2 - Descriptografar')
			while True:
				resp = int(input('Escolha uma opção: '))
				if resp == 1:		
					print('Result: >>>>>>>>> {} <<<<<<<<<'.format(encrypt_cbc(text, key, rounds)))
					break
				elif resp == 2:
					#print('Result: >>>>>>>>> {} <<<<<<<<<'.format(decrypt(text, key, rounds)))
					break
				else:
					print('Opção inválida, ', end='')
		elif resp == 3:
			pass
		elif resp == 4:
			break
		else:
			print('Opção inválida, ', end='')

main()