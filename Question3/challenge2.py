from struct import unpack

def str_xor(str1, str2):
	if len(str1) != len(str2):
		raise ValueError('Buffers must be equal length')
	else:
		result = []
		for i in xrange(len(str1)):
			(a,), (b,) = unpack('B', str1[i]), unpack('B', str2[i])
			result.append(chr(a ^ b))
		return ''.join(result).encode('hex')

if __name__ == '__main__':
	string1 = '1c0111001f010100061a024b53535009181c'
	string2 = '686974207468652062756c6c277320657965'
	print str_xor(string1.decode('hex'), string2.decode('hex'))