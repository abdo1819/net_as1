def xor(a:str, b:str) -> str:
	'''
	Performs XOR operation on two binary strings assuming 
	
	:param a: First binary string ex: '0110'
	:param b: Second binary string ex: '1100'
	:return: XOR result

	steps:
	- create loop to iterate through strings
	- if bits are equal, append 0 to result
	- else append 1 to result
	- return result as string
	
	>>> xor('0110','1100')
	'1010'

	>>> xor('10','00')
	'10'
	'''
	return '0'



def mod2div(divident:str, divisor:str)->str:
	'''
	Performs modular division on two binary strings

	:param divident: Divident string ex: '1001000'
	:param divisor: Divisor string ex: '1011'
	:return: Remainder of modular division

	steps:
	- create loop to iterate through divident
	- if first bit is 1, xor divident part with divisor
	- else xor divident part with 0
	- return remainder
	


	>>> mod2div('1001000','1011')
	'110'

	>>> mod2div('1000110','1011')
	'011'

	>>> mod2div('1001110','1011')
	'000'

	>>> mod2div('1111','101')
	'00'

	>>> mod2div('1111000','1011')
	'111'
	'''
	
	return '0'


def encodeData(data:str, key:str):
	'''
	Encodes data using CRC 

	:param data: Data to encode ex: '1001000'
	:param key: Key to use for encoding ex: '1011'
	:return: Encoded data ex: '1001000110'
	
	steps:
	- create string from data with appended zeros 
	- perform modular division using mod2div
	- append remainder to data


	>>> encodeData('1001','1011')
	'1001110'

	>>> encodeData('1111','1011')
	'1111111'
	'''

	return '0'
	
	


if __name__ == "__main__":
    import doctest
    doctest.testmod()