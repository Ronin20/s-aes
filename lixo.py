

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
'''