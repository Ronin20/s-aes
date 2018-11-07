def switch_coloumns(matriz):
	i = int(0)
	sw_coloumns = []
	for i in range(0,len(matriz)):
		sw_coloumns.append( (int(matriz[i][0],16))		 ^ 	(4 * int(matriz[i][2],16)))
		sw_coloumns.append( (4 * (int(matriz[i][0],16))) ^ 	(int (matriz[i][2],16)))
		sw_coloumns.append( (int(matriz[i][1],16))		 ^	(4 * int(matriz[i][3],16)))
		sw_coloumns.append( (4 * (int(matriz[i][1],16))) ^ 	(int (matriz[i][3],16)))
		
	return sw_coloumns

matriz = [['6', '4'], ['C', '0']]
print(switch_coloumns(matriz))