def decToHex(d):
	return '{:0>4}'.format(hex(d)[2:])

d = 10
print(decToHex(d))