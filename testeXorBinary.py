def xorBinary(a, b):
	result = int(a,2) ^ int(b,2)
	result = bin(result)
	return result[2:]

a = '1010'
b = '0101'

c = xorBinary(a, b)
print('c = {} is of type: {}'.format(c, type(c)))