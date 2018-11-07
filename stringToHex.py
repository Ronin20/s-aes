import binascii


def stringToHex(par):
	new = ''	
	new += par[0].encode("utf-8").hex()
	new += par[1].encode("utf-8").hex()
	return new

def hexToString(a, b):
	result = int(a, 16) ^ int(b, 16) # Converte para inteiro e faz o xor entre eles
	return '{:x}'.format(result)     # Converte de vola para hexadecimal

def byte_to_binary(n):
    return ''.join(str((n & (1 << i)) and 1) for i in reversed(range(8)))

def hexToBinary(hex):
    b = int(hex, 16)
    binary = bin(b)
    return binary[2:]

def binToDec(bina):
	return int(bina, 2)

print(binToDec('10'))

#xored = xor_strings('A479', '25D5').encode("hex")
#print(xored)
#print(strxor('A479', '25D5'))
#print(     hex(sth('aa')) ^ hex(sth('bb'))        )