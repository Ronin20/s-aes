def decToBin(d):
	return '{:0>4}' .format(str(bin(d))[2:])
a = 4
b = decToBin(a)
print(b)