def separa4(lista):
	processada = list()
	tmp = ''
	for c in lista:
		tmp += c
		if len(tmp) == 4:
			processada.append(tmp)
			tmp = ''
	return processada

t = '08a1f07b2c4e'
print(separa4(t))