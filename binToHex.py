def binToHex(b):
	result = hex(int(b, 2))
	return result[2:]

n = '1010'
print(binToHex(n))