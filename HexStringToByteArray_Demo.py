def main(): 
	
	print( "HexStringToByteArray_Demo" )
	
	print
	
	hexString = "FF-23-AD-A3"
	
	print("Hex String: {}" .format(hexString(hexString)))
	print("Int array: {}" .format(hexStringToIntArray( hexString )))
	print("Byte array: {}" .format(hexStringToByteArray( hexString )))
	return
	
def hexStringToIntArray( hex ):
	
	hex = hex.replace( "-", "" )
	
	result = []
	
	for i in range( 0, len(hex), 2 ):
        
		hexVal = hex[i : i+2] # sub string between i and i+2
		intVal = int(hexVal, 16)
		intStr = str(intVal)
        
		result.append( intVal )
	
	return result

def hexStringToByteArray( hex ):
	
	hex = hex.replace( "-", "" )
	
	result = []
	
	for i in range( 0, len(hex) - 1, 2 ):
		hexVal = hex[ i : i + 2 ] # sub string between i and i + 2
		intVal = int( hexVal, 16 ) # cast to integer
		binVal = bin( intVal )[ 2 : ].zfill( 8 )
		
		result.append( binVal )
	
	return result

main()













