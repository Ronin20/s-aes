def xorGeral(a, b): # Faz o xor entre dois valores hexadecimais
	result = int(a, 16) ^ int(b, 16) # Converte para inteiro e faz o xor entre eles
	return '{:0>4x}'.format(result)  # Converte de vola para hexadecimal, sempre com 4 digitos
a = 'e44a'
b = '94b6'

print(xorGeral(a, b))