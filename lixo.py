

'''
def expandirChave(chave):
	part_one = (chave[0][0] + chave[1][0])
	part_two = (chave[0][1] + chave[1][1])

	part_two = part_two[::-1] #Rotaciona, nesse caso como sao apenas duas, estou invertendo

	xor_one = xorGeral(part_one, '80')
	print('xor_one: ', hexToBinary(xor_one))
	sub1 = sub(part_two)
	print('sub 1 : ',hexToBinary(sub1))
	xor_two = xorGeral(xor_one, sub1)
	print('xor_two', hexToBinary(xor_two))

	part_three = xorGeral(xor_two, '30')
	sub2 = sub(xor_two)
	xor_three = xorGeral(part_three, sub2)
	print('xor_three: ', hexToBinary(xor_three))


def xorBinary(a, b):
	result = int(a,2) ^ int(b,2)
	result = bin(result)
	return '{}'.format(result[2:])
a = '1100'
b = '0000'
print(xorBinary(a, b))'''

def decrypt(text, key, rounds):
	text_plain = ''
	matrizEstado = list()
	matrizChave = list()
	inicio = 0
	fim = 3
	

	for p in range(len(cifrado)/4):
		parte = text[inicio, fim+1]
		inicio = fim
		fim += 3
		for i in range(1, rounds+1):
			


			#print('Round {}'.format(i))
			matrizEstado = subBytes(matrizEstado, sbox)
			#print('1 - subBytes: {}'.format(matrizEstado))
			matrizEstado = shiftRows(matrizEstado)
			#print('2 - shiftRows: {}'.format(matrizEstado))
			matrizEstado = mixColumns(matrizEstado)
			#print('3 - mixColumns: {}'.format(matrizEstado))
			matrizEstado = addRoundKey(matrizEstado, matrizChave,  decToBin(2**i))
			#print('4 - addRoundKey: {}'.format(matrizEstado))
		text_plain += concatenaMatriz(matrizEstado)



		matrizEstado = geraMatriz(par)
		#print('matrizEstado: {}'.format(matrizEstado))
		matrizChave = geraMatriz(key)
		#print('matrizChave: {}'.format(matrizChave))		
		matrizEstado = incluirChave(matrizEstado, matrizChave)
		#print('Incluindo chave na matriz...')
		#print('matrizEstado: {}'.format(matrizEstado))
		#print('Começando a rodar...')
		
	return text_plain


09/11/18
	def decrypt_cbc(text, key, rounds):
	lista_clara = ['0000']
	ind = 1
	text_plain = ''
	matrizChave = geraMatriz(key)
	chaves = generateKeys(matrizChave, rounds)
	chaves = chaves[::-1]
	print('chaves: ', chaves)
	inicio = 0
	fim = 4
	#text = inverte4(text)
	for p in range(int(len(text)/4)):
		parte = text[inicio : fim]
		inicio = fim
		fim += 4
		cif = parte
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
		matrizEstado[0][1], matrizEstado[1][0] = matrizEstado[1][0], matrizEstado[0][1]
		cif = concatenaMatriz(matrizEstado)
		lista_clara.append(cif)
		text_plain += cif
		matrizEstado = montaMatriz(xorGeral(concatenaMatriz(matrizEstado), concatenaMatriz(matrizChave)))
		'''print('ANTES: ', matrizEstado)

		matrizEstado = concatenaMatriz(matrizEstado)
		matrizEstado = xorGeral(matrizEstado, cif)
		matrizEstado = montaMatriz(matrizEstado)
		
		print('DEPOIS: ', matrizEstado)
		




	try:
		text_plain = hexToString(text_plain) 
	except:
		print('Não foi possível traduzir essa saída...')
	'''
	print(lista_clara)
	return text_plain


def encrypt_ctr(text_plain, key, rounds): # Função de criptografar o ECB
	cifrada = ''
	text_plain = text_plain.upper()
	text_plain = separa(text_plain)	
	print('-'*60)
	for par in text_plain:
		print('PAR: {}'.format(par))
		matrizEstado = geraMatriz(par)
		print('matrizEstado: {}'.format(matrizEstado))
		matrizChave = geraMatriz(key)
		print('matrizChave: {}'.format(matrizChave))		
		matrizEstado = incluirChave(matrizEstado, matrizChave)
		print('Incluindo chave na matriz...')
		print('matrizEstado: {}'.format(matrizEstado))
		print('Começando a rodar...')
		for i in range(0, rounds):
			print('ANTES: {}'.format(matrizEstado))
			matrizEstado = concatenaMatriz(matrizEstado)
			matrizEstado = xorGeral(matrizEstado, str(i))
			matrizEstado = montaMatriz(matrizEstado)
			print('DEPOIS: {}'.format(matrizEstado))
			print('Round {}'.format(i))
			matrizEstado = subBytes(matrizEstado, sbox)
			print('1 - subBytes: {}'.format(matrizEstado))
			matrizEstado = shiftRows(matrizEstado)
			print('2 - shiftRows: {}'.format(matrizEstado))
			#if i != rounds-1: #--teste--#
			matrizEstado = mixColumns(matrizEstado)
			print('3 - mixColumns: {}'.format(matrizEstado))
			matrizEstado, matrizChave = addRoundKey(matrizEstado, matrizChave,  decToBin(2**i))
			print('4 - addRoundKey: {}'.format(matrizEstado))
		cif = concatenaMatriz(matrizEstado)
		cifrada += cif
		print('-'*60)
	return cifrada



























