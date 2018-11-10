def hexToString(h):
	return bytearray.fromhex(h).decode()
h = '5553'
print(hexToString(h))