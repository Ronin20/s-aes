# coding: utf-8
'''Copyright © 2018 Ranielison Oliveira. All rights reserved.'''
#------------------------------------- Tabelas -----------------------------------
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

def binToHex(b): # Converte Binário para Hexadecimal
	result = hex(int(b, 2))
	return result[2:]

def decToBin(d): # Converte Decimal para binário
	return '{:0>4}' .format(str(bin(d))[2:])

def hexToString(h): # Converte hexadecimal para string
	return bytearray.fromhex(h).decode()

def decToHex(d):
	return '{:0>4}'.format(hex(d)[2:])
#--------------------------- Operações -----------------------------

def xorGeral(a, b): # Faz o xor entre dois valores hexadecimais
	result = int(a, 16) ^ int(b, 16) # Converte para inteiro e faz o xor entre eles
	return '{:0>4x}'.format(result)  # Converte de vola para hexadecimal, sempre com 4 digitos

def xorBinary(a, b): # Faz um xor entre valores binários
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
	mat[1][0] = msghex[1]
	mat[0][1] = msghex[2]
	mat[1][1] = msghex[3]
	return mat

def montaMatriz(simbols): # REcebe uma string e organiza ela em uma matriz 
	mat = [['', ''], ['', '']]
	mat[0][0] = simbols[0]
	mat[0][1] = simbols[1] 
	mat[1][0] = simbols[2]
	mat[1][1] = simbols[3]
	return mat

def separa(lista): # Separa uma string em pares de caracteres
	processada = list()
	tmp = list()
	if len(lista) % 2: # Se a string for de tamanho impar, insere um 0 no final
		lista += '0'
	for i in range(0,len(lista),2):
		tmp.append(lista[i])
		tmp.append(lista[i+1])
		processada.append(tmp[:])
		tmp.clear()
	return processada

def separa4(lista): # Recebe uma string de tamanho multiplo de 4 e retorna uma lista com ela fracionada em pedaos de tamanho 4
	processada = list()
	tmp = ''
	for c in lista:
		tmp += c
		if len(tmp) == 4:
			processada.append(tmp)
			tmp = ''
	return processada

#------------------------ Funções auxiliares ----------------------
def rotWord(w): # Recebe uma string e faz uma rotação nela
	return w[1:] + w[0]

def search(table, l, c): # Busca um valor em uma tabela a partir da linha e coluna
	l = int(l, 16)
	c = int(c, 16)
	return table[l][c]

def sub(par): # Faz uma substituição de Nibble
	l = par[:2] # Pega os dois primeiros digitos que serão a linha
	c = par[2:] # Pega os dois ultimos digitos que serão a coluna
	l = int(l, 2) # Converte para decimal
	c = int(c, 2)
	return hexToBinary(sbox[l][c])

def tratar_erro(): # Exibe mensagens em casos de erros não identificados
	print('o Miserável é um gênio...')
	print('Operação inválida')

#------------------------ Métodos ----------------------

def mixColumns(mat): # Faz a multiplicação das matrizes usando as tabelas GF 2⁴
	new_mat = [['', ''], ['', '']]
	new_mat[0][0] = search(addTable, mat[0][0], search(multTable, '4', mat[1][0]))
	new_mat[1][0] = search(addTable, search(multTable, '4', mat[0][0]), mat[1][0])
	new_mat[0][1] = search(addTable, mat[0][1], search(multTable, '4', mat[1][1]))
	new_mat[1][1] = search(addTable, search(multTable, '4', mat[0][1]), mat[1][1])
	return new_mat

def mixColumnsInverse(mat): # Faz a inversa da matriz usando as tabelas GF 2⁴
	new_mat = [['', ''], ['', '']]
	new_mat[0][0] = search(addTable, search(multTable, '2', mat[0][0]), search(multTable, '9', mat[1][0]))
	new_mat[1][0] = search(addTable, search(multTable, '9', mat[0][0]), search(multTable, '2', mat[1][0]))
	new_mat[0][1] = search(addTable, search(multTable, '2', mat[0][1]), search(multTable, '9', mat[1][1]))
	new_mat[1][1] = search(addTable, search(multTable, '9', mat[0][1]), search(multTable, '2', mat[1][1]))
	return new_mat

def incluirChave(mat, chave): # Inclui a chave antes de começar as rodadas
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

def shiftRows(mat): # Faz o deslocamento das linhas
	mat[1][0], mat[1][1] = mat[1][1], mat[1][0] # Apenas troca os elementos da segunda linha
	return mat

def keySchedule(key, rcon): # Recebe uma matriz chave e um rcon, e calcula a nova matriz
	ws = list()
	tmp = list()
	new_key = ''
	for i in key: # Roda a chave, convertendo cada carater para binario e inserindo em uma lista
		for j in i:
			tmp.append(hexToBinary(j))
			ws.append(tmp[:])
			tmp.clear()
	rot = rotWord(''.join(ws[3])) #Rotaciona o ultimo W
	par = sub(rot) # Substitui na sbox
	first_xor = xorBinary(''.join(ws[0]), par) # Faz um xor com o primeiro W
	second_xor = xorBinary(first_xor, rcon) # Faz um xor com o Rcon correspondente ao round atual
	tmp.append(second_xor) # Adiciona o resrultado obtido em uma lista
	ws.append(tmp[:])
	tmp.clear()
	for i in range(1, 4): # Percorre os W's existentes e faz um xor para gerar os novos
		tmp.append(xorBinary(''.join(ws[i]), ''.join(ws[i+3]))) #Faz um xor
		ws.append(tmp[:])
		tmp.clear()	
	for i in ws[4:]: # Pega somente os 4 novos W's gerados, converte pra hexa e concatena em uma string
		for j in i:
			new_key += binToHex(j) #Converte pra hexa
	return new_key

def generateKeys(chave, round): # Recebe uma chave e uma quantidade, e retorna uma lista com essas chaves
	lista_chaves = list()
	for i in range(0, round):
		chave = keySchedule(chave, decToBin(2**i))
		lista_chaves.append(chave)
		chave = montaMatriz(chave)
	return lista_chaves

def addRoundKey(mat, chave, rcon): # Encontra a chave do round e faz um xor com a saída de MixColums
	new_mat = [['', ''], ['', '']]
	
	new_key = keySchedule(chave, rcon) # Pega a chave correspondente ao round
	new_mat = xorGeral(concatenaMatriz(mat), new_key) # Faz o xor com a matriz estado atual
	
	mat[0][0] = new_mat[0]
	mat[0][1] = new_mat[1] 
	mat[1][0] = new_mat[2]
	mat[1][1] = new_mat[3]
	return mat, montaMatriz(new_key) # retorna o resultado do xor e a ultima chave usada

#---------------------- Métodos principais --------------------

def encrypt(text_plain, key, rounds): # Criptografia ECB
	cifrada = ''
	text_plain = text_plain.upper() # Coloca o texto recebido em caixa alta
	text_plain = separa(text_plain)	 # Separa o texto em pares
	print('-'*60)
	for par in text_plain: # Percorre todos os pares gerados
		print('PAR: {}'.format(par))
		matrizEstado = geraMatriz(par) # Gera a matriz do par 
		print('matrizEstado: {}'.format(matrizEstado))
		matrizChave = geraMatriz(key) # Gera a matriz da chave 
		print('matrizChave: {}'.format(matrizChave))		
		matrizEstado = incluirChave(matrizEstado, matrizChave) # Faz o xor entre matriz estado e matriz chave
		print('Incluindo chave na matriz...')
		print('matrizEstado: {}'.format(matrizEstado))
		print('Começando a rodar...')
		for i in range(0, rounds): # Começa o laço dos rounds
			print('Round {}'.format(i))
			matrizEstado = subBytes(matrizEstado, sbox) # Faz a substituição do Nibble usado a s-box
			print('1 - subBytes: {}'.format(matrizEstado))
			matrizEstado = shiftRows(matrizEstado) # Faz o deslocamento de linhas
			print('2 - shiftRows: {}'.format(matrizEstado))
			matrizEstado = mixColumns(matrizEstado) # Faz o embaralhamento de colunas
			print('3 - mixColumns: {}'.format(matrizEstado))
			# Expande e adiciona a nova chave
			matrizEstado, matrizChave = addRoundKey(matrizEstado, matrizChave,  decToBin(2**i)) 
			print('4 - addRoundKey: {}'.format(matrizEstado))
		cif = concatenaMatriz(matrizEstado) # Depois de finalizado o laço, concatena a matriz e guarda em uma string
		cifrada += cif # Concatena as strings correspondentes a saída de cada par gerada na linha acima
		print('-'*60)
	return cifrada

def decrypt(text, key, rounds): # Descriptografia ECB
	text_plain = ''
	matrizChave = geraMatriz(key) # Gera a chave
	chaves = generateKeys(matrizChave, rounds) # Gera todas as chaves que foram usadas
	chaves = chaves[::-1] # Inverte a lista de chaves

	inicio = 0
	fim = 4
	
	for p in range(int(len(text)/4)): # Faz um laço do tamanho da quantidade de pares recebidos
		parte = text[inicio : fim]
		inicio = fim
		fim += 4
		matrizEstado = montaMatriz(parte) # Monta a matriz
		for i in range(rounds): # Faz o laço de rounds fazendo o processo reverso
			matrizEstado =  montaMatriz(xorGeral(concatenaMatriz(matrizEstado), chaves[i]))
			matrizEstado = mixColumnsInverse(matrizEstado)
			matrizEstado[0], matrizEstado[1] = matrizEstado[1], matrizEstado[0]
			matrizEstado = shiftRows(matrizEstado)
			matrizEstado = subBytes(matrizEstado, sboxInverse)
		matrizEstado = montaMatriz(xorGeral(concatenaMatriz(matrizEstado), concatenaMatriz(matrizChave)))
		matrizEstado[0][1], matrizEstado[1][0] = matrizEstado[1][0], matrizEstado[0][1]
		text_plain += concatenaMatriz(matrizEstado)
	
	try: # Tenta converter na tabela ascci
		text_plain = hexToString(text_plain) 
	except: # Caso não consiga
		print('Não foi possível traduzir essa saída...')
	
	return text_plain


def encrypt_cbc(text_plain, key, rounds): # Criptografia CBC
	cifrada = ''
	cif = '0000'
	text_plain = text_plain.upper()
	text_plain = separa(text_plain)	
	print('-'*60)
	for par in text_plain:
		print('PAR: {}'.format(par))
		matrizEstado = geraMatriz(par) # Gera a matriz estado inicial
		matrizEstado = concatenaMatriz(matrizEstado) # Concatena ela em uma string
		matrizEstado = xorGeral(matrizEstado, cif) # Faz o xor dela com cif, que inicialmente é 0000, mas atualiza
		matrizEstado = montaMatriz(matrizEstado) # Depois do xor monta a matriz novamente
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
		cif = concatenaMatriz(matrizEstado) # Nesse ponto, cif é sempre a saída do par, que será somada com a proxima entrada
		cifrada += cif
		print('-'*60)
	return cifrada

def decrypt_cbc(text, key, rounds): # Descriptografia CBC
	text_plain = '' # String que receberá a saída final
	lista_cifs = [] # Lista para guardar as soluções parciais
	matrizChave = geraMatriz(key) # Gera a chave
	chaves = generateKeys(matrizChave, rounds) # Gera uma lista de chaves
	chaves = chaves[::-1]

	inicio = 0
	fim = 4
	
	for p in range(int(len(text)/4)):
		parte = text[inicio : fim]
		inicio = fim
		fim += 4
		matrizEstado = montaMatriz(parte)
		for i in range(rounds):
			matrizEstado =  montaMatriz(xorGeral(concatenaMatriz(matrizEstado), chaves[i]))
			matrizEstado = mixColumnsInverse(matrizEstado)
			matrizEstado[0], matrizEstado[1] = matrizEstado[1], matrizEstado[0]
			matrizEstado = shiftRows(matrizEstado)
			matrizEstado = subBytes(matrizEstado, sboxInverse)
		matrizEstado = montaMatriz(xorGeral(concatenaMatriz(matrizEstado), concatenaMatriz(matrizChave)))
		#matrizEstado[0][1], matrizEstado[1][0] = matrizEstado[1][0], matrizEstado[0][1]
		cif = concatenaMatriz(matrizEstado)
		lista_cifs.append(cif)

	text = '0000' + text # Coloca 0000 no inicio do texto recebido apenas para servir de elemento neutro na soma
	text = separa4(text) # Separa o texto em pedaços de tamanho 4 

	for p in range(len(lista_cifs)): # faz um laço para percorrer e somar os elementos das duas listas
		fatia = montaMatriz(xorGeral(lista_cifs[p], text[p])) # Monta a matriz a partir do xor
		fatia[0][1], fatia[1][0] = fatia[1][0], fatia[0][1] # Troca a posição do nibble
		fatia = concatenaMatriz(fatia) # Concatena a matriz novamente
		text_plain += fatia # Concatena na string de saída
	
	try: # Tenta converter na tabela ascci
		text_plain = hexToString(text_plain) 
	except: # Caso não consiga
		print('Não foi possível traduzir essa saída...')
		
	return text_plain

def encrypt_ctr(text_plain, key, rounds): # Criptografia CTR
	cifrada = ''
	cif = '0001' # Contador inicialmente em 1
	text_plain = text_plain.upper()
	text_plain = separa(text_plain)	

	print('-'*60)
	for n, par in enumerate(text_plain): # Faz um laço pra percorrer cada par e os enumera pra usar o contador
		print('PAR: {}'.format(par))
		matrizEstado = geraMatriz(par) # Gera a matriz estado
		
		#Faz um xor com o contador
		matrizEstado = concatenaMatriz(matrizEstado)
		matrizEstado = xorGeral(matrizEstado, cif)
		matrizEstado = montaMatriz(matrizEstado)
		
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
		cif = decToHex(n+2) # Atualiza o contador para fazer a soma no proximo par
		print('-'*60)
	return cifrada

def decrypt_ctr(text, key, rounds): # Descriptografia CTR
	text_plain = ''
	lista_cifs = []
	count_list = list()
	matrizChave = geraMatriz(key)
	chaves = generateKeys(matrizChave, rounds)
	chaves = chaves[::-1]

	inicio = 0
	fim = 4
	
	for p in range(int(len(text)/4)):
		parte = text[inicio : fim]
		inicio = fim
		fim += 4
		matrizEstado = montaMatriz(parte)
		for i in range(rounds):
			matrizEstado =  montaMatriz(xorGeral(concatenaMatriz(matrizEstado), chaves[i]))
			matrizEstado = mixColumnsInverse(matrizEstado)
			matrizEstado[0], matrizEstado[1] = matrizEstado[1], matrizEstado[0]
			matrizEstado = shiftRows(matrizEstado)
			matrizEstado = subBytes(matrizEstado, sboxInverse)
		matrizEstado = montaMatriz(xorGeral(concatenaMatriz(matrizEstado), concatenaMatriz(matrizChave)))
		cif = concatenaMatriz(matrizEstado)
		lista_cifs.append(cif)
	for i in range(1, len(lista_cifs)+1):
		count_list.append(decToHex(i))

	#print('lista_cifs: {}'.format(lista_cifs))
	#print('count_list: {}'.format(count_list))

	for p in range(len(lista_cifs)):
		fatia = montaMatriz(xorGeral(lista_cifs[p], count_list[p]))
		fatia[0][1], fatia[1][0] = fatia[1][0], fatia[0][1]
		fatia = concatenaMatriz(fatia)
		text_plain += fatia
	
	try:
		text_plain = hexToString(text_plain) 
	except:
		print('Não foi possível traduzir essa saída...')
		
	return text_plain

#---------------------- Função principal --------------------

def main ():
	matrizEstado = list()
	matrizChave = list()
	while True:
		text = input('Digite o texto: ')
		key = input('Digite a chave de encriptação: ').upper()
		if len(key) % 2: # Verifica se a chave é impar, se for adiciona um 0 no final
			key += '0'
		key = key[:2] # Trunca a chave para o tamanho de 2 caracteres(16 bits)
		
		while True: # Validação da quantidade de rounds recebidos
			try:
				rounds = int(input('Quantidade de rounds [1 - 4]: '))
			except:
				tratar_erro()
			if 0 < rounds < 5:
				break
			else:
				print('Quantidade inválida, ', end='')

		print('1 - S-Aes ECB')
		print('2 - S-Aes CBC')
		print('3 - S-Aes CTR')
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
					try:
						print('Result: >>>>>>>>> {} <<<<<<<<<'.format(decrypt(text, key, rounds)))
					except:
						tratar_erro()
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
					try:
						print('Result: >>>>>>>>> {} <<<<<<<<<'.format(decrypt_cbc(text, key, rounds)))
					except:
						tratar_erro()
					break
				else:
					print('Opção inválida, ', end='')
		elif resp == 3:
			print('1 - Criptografar')
			print('2 - Descriptografar')
			while True:
				resp = int(input('Escolha uma opção: '))
				if resp == 1:		
					print('Result: >>>>>>>>> {} <<<<<<<<<'.format(encrypt_ctr(text, key, rounds)))
					break
				elif resp == 2:
					try:
						print('Result: >>>>>>>>> {} <<<<<<<<<'.format(decrypt_ctr(text, key, rounds)))
					except:
						tratar_erro()
					break
				else:
					print('Opção inválida, ', end='')
		while True:
			continua = input('Deseja continuar? S/N: ')
			if continua in 'SsNn' and len(continua) == 1:
				break
			else:
				print('Resposta inválida', end='')
		if continua in 'Nn':
			break
	print('Copyright © 2018 Ranielison Oliveira. All rights reserved.')
main()