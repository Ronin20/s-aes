import binascii


sbox = [['9', '4', 'A', 'B'], ['D', '1', '8', '5'], ['6', '2', '0', '3'], ['C', 'E', 'F', '7']]
sboxInverse = [['A', '5', '9', 'B'], ['1', '7', '8', 'F'], ['6', '0', '2', '3'], ['C', '4', 'D', 'E']]

def stringToHex(par): #Converte uma string para Hexadecimal
	new = ''	
	new += par[0].encode("utf-8").hex()
	new += par[1].encode("utf-8").hex()
	return new

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def separa(lista):
	processada = list()
	tmp = list()
	for i in range(0,len(lista),2):
		tmp.append(lista[i])
		tmp.append(lista[i+1])
		processada.append(tmp[:])
		tmp.clear()
	return processada

def round(par):
	bloco = [[0, 0, 0, 0], [0, 0, 0, 0], 
			[0, 0, 0, 0], [0, 0, 0, 0]]
	
	concatena = text_to_bits(par[0])
	concatena += text_to_bits(par[1])
	
	ind = 0
	for i in range(4):
		for j in range(4):
			bloco[i][j] = concatena[ind]
			ind += 1
	
	bloco[1], bloco[2] = bloco[2], bloco[1]
	
	print(bloco)

def incluir_chave(mat, chave):
	


palavra = input('Digite uma palavra: ')
processada = separa(palavra)
round(processada[0])

