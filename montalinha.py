entrada = input()
linha = '['
for i in entrada:
	linha += "'" + i + "', "
linha += '],'
print(linha)