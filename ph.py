import numpy as np

addTable = {
		'00': '0', '01':'1', '02':'2', '03':'3', '04':'4', '05':'5', '06':'6', '07':'7', '08':'8', '09':'9', '0a':'a', '0b':'b', '0c':'c', '0d':'d', '0e':'e', '0f':'f',
		'10': '1', '11':'0', '12':'3', '13':'2', '14':'5', '15':'4', '16':'7', '17':'6', '18':'9', '19':'8', '1a':'b', '1b':'a', '1c':'d', '1d':'c', '1e':'f', '1f':'e', 
        '20': '2', '21':'3', '22':'0', '23':'1', '24':'6', '25':'7', '26':'4', '27':'5', '28':'a', '29':'b', '2a':'8', '2b':'9', '2c':'e', '2d':'f', '2e':'c', '2f':'d',
        '30': '3', '31':'2', '32':'1', '33':'0', '34':'7', '35':'6', '36':'5', '37':'4', '38':'b', '39':'a', '3a':'9', '3b':'8', '3c':'f', '3d':'e', '3e':'d', '3f':'c',
        '40': '4', '41':'5', '42':'6', '43':'7', '44':'0', '45':'1', '46':'2', '47':'3', '48':'c', '49':'d', '4a':'e', '4b':'f', '4c':'8', '4d':'9', '4e':'a', '4f':'b',
        '50': '5', '51':'4', '52':'7', '53':'6', '54':'1', '55':'0', '56':'3', '57':'2', '58':'d', '59':'c', '5a':'f', '5b':'e', '5c':'9', '5d':'8', '5e':'b', '5f':'a',
        '60': '6', '61':'7', '62':'4', '63':'5', '64':'2', '65':'3', '66':'0', '67':'1', '68':'e', '69':'f', '6a':'c', '6b':'d', '6c':'a', '6d':'b', '6e':'8', '6f':'9',
        '70': '7', '71':'6', '72':'5', '73':'4', '74':'3', '75':'2', '76':'1', '77':'0', '78':'f', '79':'e', '7a':'d', '7b':'c', '7c':'b', '7d':'a', '7e':'9', '7f':'8',
        '80': '8', '81':'9', '82':'a', '83':'b', '84':'c', '85':'d', '86':'e', '87':'f', '88':'0', '89':'1', '8a':'2', '8b':'3', '8c':'4', '8d':'5', '8e':'6', '8f':'7',
        '90': '9', '91':'8', '92':'b', '93':'a', '94':'d', '95':'c', '96':'f', '97':'e', '98':'1', '99':'0', '9a':'3', '9b':'2', '9c':'5', '9d':'4', '9e':'7', '9f':'6',
        'a0': 'a', 'a1':'b', 'a2':'8', 'a3':'9', 'a4':'e', 'a5':'f', 'a6':'c', 'a7':'d', 'a8':'2', 'a9':'3', 'aa':'0', 'ab':'1', 'ac':'6', 'ad':'7', 'ae':'4', 'af':'5',
        'b0': 'b', 'b1':'a', 'b2':'9', 'b3':'8', 'b4':'f', 'b5':'e', 'b6':'d', 'b7':'c', 'b8':'3', 'b9':'2', 'ba':'1', 'bb':'0', 'bc':'7', 'bd':'6', 'be':'5', 'bf':'4',
        'c0': 'c', 'c1':'d', 'c2':'e', 'c3':'f', 'c4':'8', 'c5':'9', 'c6':'a', 'c7':'b', 'c8':'4', 'c9':'5', 'ca':'6', 'cb':'7', 'cc':'0', 'cd':'1', 'ce':'2', 'cf':'3',
        'd0': 'd', 'd1':'c', 'd2':'f', 'd3':'e', 'd4':'9', 'd5':'8', 'd6':'b', 'd7':'a', 'd8':'5', 'd9':'4', 'da':'7', 'db':'6', 'dc':'1', 'dd':'0', 'de':'3', 'df':'2',
        'e0': 'e', 'e1':'f', 'e2':'c', 'e3':'d', 'e4':'a', 'e5':'b', 'e6':'8', 'e7':'9', 'e8':'6', 'e9':'7', 'ea':'4', 'eb':'5', 'ec':'2', 'ed':'3', 'ee':'0', 'ef':'1',
        'f0': 'f', 'f1':'e', 'f2':'d', 'f3':'c', 'f4':'b', 'f5':'a', 'f6':'9', 'f7':'8', 'f8':'7', 'f9':'6', 'fa':'5', 'fb':'4', 'fc':'3', 'fd':'2', 'fe':'1', 'ff':'0',   
	}
multTable = {
		'00': '0', '01':'0', '02':'0', '03':'0', '04':'0', '05':'0', '06':'0', '07':'0', '08':'0', '09':'0', '0a':'0', '0b':'0', '0c':'0', '0d':'0', '0e':'0', '0f':'0',
		'10': '0', '11':'1', '12':'2', '13':'3', '14':'4', '15':'5', '16':'6', '17':'7', '18':'8', '19':'9', '1a':'a', '1b':'b', '1c':'c', '1d':'d', '1e':'e', '1f':'f', 
        '20': '0', '21':'2', '22':'4', '23':'6', '24':'8', '25':'a', '26':'c', '27':'e', '28':'3', '29':'1', '2a':'7', '2b':'5', '2c':'b', '2d':'9', '2e':'f', '2f':'d',
        '30': '0', '31':'3', '32':'6', '33':'5', '34':'c', '35':'f', '36':'a', '37':'9', '38':'b', '39':'8', '3a':'d', '3b':'e', '3c':'7', '3d':'4', '3e':'1', '3f':'2',
        '40': '0', '41':'4', '42':'8', '43':'c', '44':'3', '45':'7', '46':'b', '47':'f', '48':'6', '49':'2', '4a':'e', '4b':'a', '4c':'5', '4d':'1', '4e':'d', '4f':'9',
        '50': '0', '51':'5', '52':'a', '53':'f', '54':'7', '55':'2', '56':'d', '57':'8', '58':'e', '59':'b', '5a':'4', '5b':'1', '5c':'9', '5d':'c', '5e':'3', '5f':'6',
        '60': '0', '61':'6', '62':'c', '63':'a', '64':'b', '65':'d', '66':'7', '67':'1', '68':'5', '69':'3', '6a':'9', '6b':'f', '6c':'e', '6d':'8', '6e':'2', '6f':'4',
        '70': '0', '71':'7', '72':'e', '73':'9', '74':'f', '75':'8', '76':'1', '77':'6', '78':'d', '79':'a', '7a':'3', '7b':'4', '7c':'2', '7d':'5', '7e':'c', '7f':'b',
        '80': '0', '81':'8', '82':'3', '83':'b', '84':'6', '85':'e', '86':'5', '87':'d', '88':'c', '89':'4', '8a':'f', '8b':'7', '8c':'a', '8d':'2', '8e':'9', '8f':'1',
        '90': '0', '91':'9', '92':'1', '93':'8', '94':'2', '95':'b', '96':'3', '97':'a', '98':'4', '99':'d', '9a':'5', '9b':'c', '9c':'6', '9d':'f', '9e':'7', '9f':'e',
        'a0': '0', 'a1':'a', 'a2':'7', 'a3':'d', 'a4':'e', 'a5':'4', 'a6':'9', 'a7':'3', 'a8':'f', 'a9':'5', 'aa':'8', 'ab':'2', 'ac':'1', 'ad':'b', 'ae':'6', 'af':'c',
        'b0': '0', 'b1':'b', 'b2':'5', 'b3':'e', 'b4':'a', 'b5':'1', 'b6':'f', 'b7':'4', 'b8':'7', 'b9':'c', 'ba':'2', 'bb':'9', 'bc':'d', 'bd':'6', 'be':'8', 'bf':'3',
        'c0': '0', 'c1':'c', 'c2':'b', 'c3':'7', 'c4':'5', 'c5':'9', 'c6':'e', 'c7':'2', 'c8':'a', 'c9':'6', 'ca':'1', 'cb':'d', 'cc':'f', 'cd':'3', 'ce':'4', 'cf':'8',
        'd0': '0', 'd1':'d', 'd2':'9', 'd3':'4', 'd4':'1', 'd5':'c', 'd6':'8', 'd7':'5', 'd8':'2', 'd9':'f', 'da':'b', 'db':'6', 'dc':'3', 'dd':'e', 'de':'a', 'df':'7',
        'e0': '0', 'e1':'e', 'e2':'f', 'e3':'1', 'e4':'d', 'e5':'3', 'e6':'2', 'e7':'c', 'e8':'9', 'e9':'7', 'ea':'6', 'eb':'8', 'ec':'4', 'ed':'a', 'ee':'b', 'ef':'5',
        'f0': '0', 'f1':'f', 'f2':'d', 'f3':'2', 'f4':'9', 'f5':'6', 'f6':'4', 'f7':'b', 'f8':'1', 'f9':'e', 'fa':'c', 'fb':'3', 'fc':'8', 'fd':'7', 'fe':'5', 'ff':'a',
	}

addTable1 = [
		['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'],
		['1', '0', '3', '2', '5', '4', '7', '6', '9', '8', 'b', 'a', 'd', 'c', 'f', 'e'],
		['2', '3', '0', '1', '6', '7', '4', '5', 'a', 'b', '8', '9', 'e', 'f', 'c', 'd'],
		['3', '2', '1', '0', '7', '6', '5', '4', 'b', 'a', '9', '8', 'f', 'e', 'd', 'c'],
		['4', '5', '6', '7', '0', '1', '2', '3', 'c', 'd', 'e', 'f', '8', '9', 'a', 'b'],
		['5', '4', '7', '6', '1', '0', '3', '2', 'd', 'c', 'f', 'e', '9', '8', 'b', 'a'],
		['6', '7', '4', '5', '2', '3', '0', '1', 'e', 'f', 'c', 'd', 'a', 'b', '8', '9'],
		['7', '6', '5', '4', '3', '2', '1', '0', 'f', 'e', 'd', 'c', 'b', 'a', '9', '8'],
		['8', '9', 'a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7'],
		['9', '8', 'b', 'a', 'd', 'c', 'f', 'e', '1', '0', '3', '2', '5', '4', '7', '6'],
		['a', 'b', '8', '9', 'e', 'f', 'c', 'd', '2', '3', '0', '1', '6', '7', '4', '5'],
		['b', 'a', '9', '8', 'f', 'e', 'd', 'c', '3', '2', '1', '0', '7', '6', '5', '4'],
		['c', 'd', 'e', 'f', '8', '9', 'a', 'b', '4', '5', '6', '7', '0', '1', '2', '3'],
		['d', 'c', 'f', 'e', '9', '8', 'b', 'a', '5', '4', '7', '6', '1', '0', '3', '2'],
		['e', 'f', 'c', 'd', 'a', 'b', '8', '9', '6', '7', '4', '5', '2', '3', '0', '1'],
		['f', 'e', 'd', 'c', 'b', 'a', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0'],
	]
multTable1 = [
		['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
		['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'],
		['0', '2', '4', '6', '8', 'a', 'c', 'e', '3', '1', '7', '5', 'b', '9', 'f', 'd'],
		['0', '3', '6', '5', 'c', 'f', 'a', '9', 'b', '8', 'd', 'e', '7', '4', '1', '2'],
		['0', '4', '8', 'c', '3', '7', 'b', 'f', '6', '2', 'e', 'a', '5', '1', 'd', '9'],
		['0', '5', 'a', 'f', '7', '2', 'd', '8', 'e', 'b', '4', '1', '9', 'c', '3', '6'],
		['0', '6', 'c', 'a', 'b', 'd', '7', '1', '5', '3', '9', 'f', 'e', '8', '2', '4'],
		['0', '7', 'e', '9', 'f', '8', '1', '6', 'd', 'a', '3', '4', '2', '5', 'c', 'b'],
		['0', '8', '3', 'b', '6', 'e', '5', 'd', 'c', '4', 'f', '7', 'a', '2', '9', '1'],
		['0', '9', '1', '8', '2', 'b', '3', 'a', '4', 'd', '5', 'c', '6', 'f', '7', 'e'],
		['0', 'a', '7', 'd', 'e', '4', '9', '3', 'f', '5', '8', '2', '1', 'b', '6', 'c'],
		['0', 'b', '5', 'e', 'a', '1', 'f', '4', '7', 'c', '2', '9', 'd', '6', '8', '3'],
		['0', 'c', 'b', '7', '5', '9', 'e', '2', 'a', '6', '1', 'd', 'f', '3', '4', '8'],
		['0', 'd', '9', '4', '1', 'c', '8', '5', '2', 'f', 'b', '6', '3', 'e', 'a', '7'],
		['0', 'e', 'f', '1', 'd', '3', '2', 'c', '9', '7', '6', '8', '4', 'a', 'b', '5'],
		['0', 'f', 'd', '2', '9', '6', '4', 'b', '1', 'e', 'c', '3', '8', '7', '5', 'a'],
	]
s_box_16 = {
		'0000': '9', '0001': '4', '0010': 'a', '0011': 'b',
		'0100': 'd', '0101': '1', '0110': '8', '0111': '5',
		'1000': '6', '1001': '2', '1010': '0', '1011': '3',
		'1100': 'c', '1101': 'e', '1110': 'f', '1111': '7', 
    }

s_invertida_box_16 = {
		'0000': 'a', '0001': '5', '0010': '9', '0011': 'b',
		'0100': '1', '0101': '7', '0110': '8', '0111': 'f',
		'1000': '6', '1001': '0', '1010': '2', '1011': '3',
		'1100': 'c', '1101': '4', '1110': 'd', '1111': 'e', 
    }
def switch_box(matriz):
	for key in s_box_16:
		if matriz == key:
			return s_box_16[key]


def dividir(mensagem,tam_grupo,tam_total):
	matriz_dividida=[]
	i = int(0)
	for x in range(tam_total):			
	    matriz_dividida.append(mensagem[i:i+tam_grupo])
	    i=i+tam_grupo

	for unused in range(len(matriz_dividida)):			# Remover os espaços em branco
		if "" in matriz_dividida:
			matriz_dividida.remove("")

	return matriz_dividida

def juntar_matriz(matriz):	
	matriz_junta = "".join(matriz)
	return matriz_junta

def StrToHexa(mensagem):
	hexadecimal = []
	i = int(0)
	for x in range(0,len(mensagem) // 2+1):			# Transformar a mensagem em Hexadecimal
	    hexadecimal.append(mensagem[i:i+2].encode("utf-8").hex())
	    i=i+2

	for unused in range(len(hexadecimal)):			# Remover os espaços em branco
	    if "" in hexadecimal:
	        hexadecimal.remove("")
	
	return hexadecimal

def Check_4_bits(matriz, hexadecimal):
	i = int(0)
	resto = int(0)
	parte_digrafo_falta = []

	if len(matriz) % 4 != 0:						# Checar se os blocos do Texto estão com 4 caracteres
		resto = len(matriz) % 4
	stop = 4 - resto;
	# print("Stop",stop)
	if resto > 0:									# Se não tiver, complementa com o final do bloco anterior
		for i in range(resto,resto+stop):
			aux = matriz[::-1][i]
			parte_digrafo_falta.append(aux)
		for i in range(0,len(parte_digrafo_falta)):
			aux = parte_digrafo_falta[::-1][i]
			hexadecimal.append(aux)
	return hexadecimal

def zero_complement(tam_blocos, bloco_16):
	
	i = int(0)
	j = int(0)
	tmp = list(bloco_16)
	while i < tam_blocos:				# Completa com 0 nos blocos com menos de 4 elementos
		if(len(bloco_16[i]) < 4):
			elemento = bloco_16[i]
			tam = 4 - len(bloco_16[i])
			for x in range(0,tam):
				elemento = '0'+ elemento
				del(tmp[i])
				tmp.insert(i,elemento)
		i+=1
		j=0
	return tmp

def switch_position(bloco):
	lista = []
	aux0 = bloco[0]
	aux1 = bloco[1]
	aux2 = bloco[2]
	aux3 = bloco[3]
	# print("Bloco",bloco)
	lista.append(aux0)
	lista.append(aux2)
	lista.append(aux1)
	lista.append(aux3)
	# print(lista)
	lista = juntar_matriz(lista)
	# print(lista)
	return lista

def xor_key(tam, mensagem,chave):
	
	xor_inicial = []
	xor_final = []

	for x in range(0,tam):		# Xor entre o bloco e a chave
		xor_inicial = hex(int(mensagem[x],16) ^ int(chave,16))
		xor_inicial = xor_inicial.replace("0x","")
		xor_final.append(xor_inicial)
	return xor_final

def StrToBin(mensagem):
	scale = 16 								# equals to hexadecimal
	num_of_bits = 4
	binario = []
	
	for x in range(len(mensagem)):			# Transformação em Binário
		binario = bin(int(str(mensagem[x]), scale))[2:].zfill(num_of_bits)
	binario = juntar_matriz(binario)
	print("Aqui", binario)
	return binario

def switch_lines(elemento):
	bloco = []
	aux0 = elemento[0]
	aux1 = elemento[1]
	bloco = aux1 + aux0
	
	return bloco

def switch_coloumns(matriz):
	sw_coloumns = []
	# print("0",matriz[0][0])
	# print("1",matriz[0][1])
	# print("2",matriz[1][0])
	# print("3",matriz[1][1])
	aux0 = int(matriz[0][0],16)
	aux1 = int(matriz[0][1],16)
	aux2 = int(matriz[1][0],16)
	aux3 = int(matriz[1][1],16)
	# sw_coloumns[0][0] = (search_dict(matriz[0][0],1)) 	  	+ int((4*(search_dict(matriz[1][0],2))))
	# sw_coloumns[0][1] = (4 * int((search_dict(matriz[0][0],2)))) +  (search_dict(matriz[1][0],1)) 
	# sw_coloumns[1][0] = (search_dict(matriz[0][1],1)) 	  	+ int((4*(search_dict(matriz[1][1],2))))
	# sw_coloumns[1][1] = (4 * int((search_dict(matriz[0][1],2)))) +  (search_dict(matriz[1][1],1)) 
	
	sw_coloumns[0][0] = search_dict((search_dict(aux0,1)), (search_dict(aux2,2)))
	sw_coloumns[0][1] = search_dict((search_dict(aux0,2)), (search_dict(aux2,1))) 
	sw_coloumns[1][0] = search_dict((search_dict(aux1,1)), (search_dict(aux3,2)))
	sw_coloumns[1][1] = search_dict((search_dict(aux1,2)), (search_dict(aux3,1))) 
	
	return sw_coloumns
def search(table, l, c):
	l = int(l, 16)
	c = int(c, 16)
	return table[l][c]

def multiMatriz(mat):
	new_mat = [['', ''], ['', '']]
	new_mat[0][0] = search(addTable1, mat[0][0], search(multTable1, '4', mat[1][0]))
	new_mat[0][1] = search(addTable1, search(multTable1, '4', mat[0][0]), mat[1][0])
	new_mat[1][0] = search(addTable1, mat[0][1], search(multTable1, '4', mat[1][1]))
	new_mat[1][1] = search(addTable1, search(multTable1, '4', mat[0][1]), mat[1][1])
	return new_mat

def search_dict(num, op):
	num = int (num,16)
	if op == 1:
		for key in addTable:
			if num == key:
				return addTable[key]
	else :
		num = num * 4
		for key in multTable:
			if num == key:
				return multTable[key]

def rotword(bloco):
	lista = []
	aux0 = bloco[3]
	aux1 = bloco[0]
	aux2 = bloco[1]
	aux3 = bloco[2]
	lista.append(aux0)
	lista.append(aux1)
	lista.append(aux2)
	lista.append(aux3)
	lista = juntar_matriz(lista)
	return lista

def make_key(chave):
	num_rodada = int(3)
	i = int(0)
	scale = 16 								# equals to hexadecimal
	num_of_bits = 4
	lista_chave = []
	temp = int(0)
	lista_chave.append(bin(int(str(chave[0]), scale))[2:].zfill(num_of_bits))
	lista_chave.append(bin(int(str(chave[1]), scale))[2:].zfill(num_of_bits))
	lista_chave.append(bin(int(str(chave[2]), scale))[2:].zfill(num_of_bits))
	lista_chave.append(bin(int(str(chave[3]), scale))[2:].zfill(num_of_bits))
	for i in range(4,12):
		temp = lista_chave[i-1]
		if i < 8:
			r = int(1)
			r1 = bin(int(str(r), scale))[2:].zfill(num_of_bits)
			# print("R1",r1)
		else:
			r = int(2)
			r1 = bin(int(str(r), scale))[2:].zfill(num_of_bits)
		
		if i % 4 == 0:
			temp = int(switch_box(rotword(temp))) ^ int(r1)
			temp = bin(int(str(temp), scale))[2:].zfill(num_of_bits)
			lista_chave.append(temp)
		else:
			temp = lista_chave[i-1]
			aux = (int((lista_chave[i-1]))) ^ (int((temp)))
			aux = bin(int(str(aux), scale))[2:].zfill(num_of_bits)
			lista_chave.append(aux)
	return lista_chave

def encrypt(mensagem,chave):
	print("Mensagem",mensagem)
	print("Chave",chave)
	# i = int(0)
	# resto = int(0)
	
	scale = 16 								# equals to hexadecimal
	num_of_bits = 4

	saida_Sbox = []
	sw_line = []
	sw_position = []
	tam_blocos = len(mensagem)
	
	for x in range(0,len(mensagem)):		# Troca as posições do Texto
		sw_position.append(switch_position(mensagem[x]))
	print("SW position\n",sw_position)

	xor = xor_key(len(mensagem), sw_position, chave)	# Xor entre o bloco e a chave

	print("Xor:\n",xor)
	tmp = list(xor)

	tmp = zero_complement(tam_blocos,tmp)		# Completa com 0 nos blocos com menos de 4 elementos	

	print("Complemento com 0\n",tmp)
	bloco2 = juntar_matriz(tmp)				
	bloco_2 = dividir(bloco2,1,len(bloco2))

	for x in range(len(bloco_2)):			# Transformação em Binário
		binario = bin(int(str(bloco_2[x]), scale))[2:].zfill(num_of_bits)
		saida_Sbox.append(switch_box(binario))
	saida_Sbox = juntar_matriz(saida_Sbox)	# Função da Caixa S
	
	saida_Sbox = juntar_matriz(saida_Sbox)	

	print("S-box\n",saida_Sbox)
	s_box_4 = dividir(saida_Sbox,2,len(saida_Sbox))
	
	s_box_4_junta = juntar_matriz(s_box_4)
	
	for x in range(0,len(s_box_4)):
		if x % 2 != 1:
			sw_line.append(s_box_4[x])
		else:
			sw_line.append(switch_lines(s_box_4[x]))
	
	print("Switch Linhas",sw_line)
	s_box_4 = dividir(juntar_matriz(sw_line),2,len(s_box_4))
	
	sw_coloum = []
	
	tam2 = int(len(sw_line)/2)
	line_dividido = dividir(sw_line,2,tam2)
	
	for x in range(tam2):
		sw_coloum.append(multiMatriz(line_dividido[x]))

	print("Switch Colunas",sw_coloum)
	
	saida = ""
	for i in sw_coloum:
		for j in i:
			for k in j:
				saida += k
	# print("Saida1",saida)
	
	return saida


def pre_processing(mensagem,chave):
	i = int(0)
	resto = int(0)
	scale = 16 								# equals to hexadecimal
	num_of_bits = 4
	chave_inicial = chave
	
	hexadecimal = []
	chave_hexa = []
	matriz_chave = []
	matriz_blocos = []
	
	hexadecimal = StrToHexa(mensagem)				# Transformar a Mensagem em Hexadecimal
	
	print("Mensagem em Hexadecimal:\n", hexadecimal)	
	matriz = juntar_matriz(hexadecimal)
	
	chave_hexa = StrToHexa(chave)					# Transformar a chave em Hexadecimal
	matriz_chave = juntar_matriz(chave_hexa)
	
	print("Chave em Hexadecimal:\n", chave_hexa)

	for x in range(0,len(chave_hexa)):				# Troca as posições da Chave
		chave_hexa = switch_position(chave_hexa[x])
	
	make_key(chave_hexa)
	
	print("Nova chave em Hexadecimal:\n", chave_hexa)
	
	matriz_chave = juntar_matriz(chave_hexa)
	
	hexadecimal = Check_4_bits(matriz, hexadecimal)	# Checa se cada bloco possui 4 bits
	matriz = juntar_matriz(hexadecimal)				# Juntar os blocos

	matriz_blocos = dividir(matriz,4,len(matriz))
	matriz = juntar_matriz(matriz_blocos)

	matriz_final_junta = juntar_matriz(matriz_blocos)
	
	matriz_final_junta = "".join(matriz_blocos)
	print("Matriz com Blocos de 16 bits com o complemento do Bloco:\n",matriz_blocos)

	tam_blocos = len(matriz_blocos)
	chave = make_key(matriz_chave)
	return matriz_blocos, chave

# ================================================================================

#									CHAMAR O PIPELINE							 #

# ================================================================================

def pipeline(mensagem,chave,text_claro,chave_inicial,op):
	chave1 = ""
	chave2 = ""
	chave3 = ""
	if op == 1:			# Encriptação
		for x in range(0,12):
			if x >= 0 and x < 4:
				aux = int(chave[x],2)
				chave1 += str(aux)
			if x > 3 and x < 8:
				aux = int(chave[x],2)
				chave2 += str(aux)
			if x > 7:
				aux = int(chave[x],2)
				chave3 += str(aux)
		print("[Criptografar]")
		print("\n=== Rodada Inicial ===\n")
		print("Entrada[",text_claro,"]")
		print("Chave[",chave_inicial,"]\n")

		pri_rodada = encrypt(mensagem,chave1)
		print("\n=== Primeira Rodada ===\n",pri_rodada,"\n")
		
		pri_rodada = dividir(pri_rodada,4,len(pri_rodada))
		seg_rodada = encrypt(pri_rodada,chave2)

		print("\n=== Segunda Rodada ===\n",seg_rodada,"\n")
		
		seg_rodada = dividir(seg_rodada,4,len(seg_rodada))
		ter_rodada = encrypt(seg_rodada,chave3)

		print("\n=== Terceira Rodada ===\n",ter_rodada,"\n")
	else:				# DEcriptação
		print("[Descriptografar]")
		print("Em construção")

def main():
    op = int(input("Criptografia AES!\nDigite:\n1 - Criptografar Mensagem\n2 - Descriptografar Mensagem\n"))
    
    if op == 1:
        print("[Criptografar]")
        # mensagem = input('Digite a mensagem:\n')
        # chave = input('Digite a chave[Ela deve possuir dois caracteres]:\n')
        # if len(chave) != 2:
        # 	while len(chave) != 2:
        # 		chave = input('Chave Errada! Digite a chave novamente com DOIS caracteres:\n')
        mensagem = 'FERIADO'
        chave = 'AB'
        
        pre = pre_processing(mensagem,chave)
        pipeline(pre[0],pre[1],mensagem,chave,1)
        # print(pre[1])

    elif op == 2:
        print("[Descriptografar]")
        # mensagem = input('Digite a mensagem:\n')
        # chave = input('Digite a chave[Ela deve possuir dois caracteres]:\n')
        # if len(chave) != 2:
        # 	while len(chave) != 2:
        # 		chave = input('Chave Errada! Digite a chave novamente com DOIS caracteres:\n')
        mensagem = 'FERIADO'
        chave = 'AB'
        
        pre = pre_processing(mensagem,chave)
        pipeline(pre[0],pre[1],mensagem,chave,2)
    else:
        print('Opção Inválida!')
