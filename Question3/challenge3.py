from collections import Counter
from struct import unpack

def find_key(string):
	tmp = []
	for i in xrange(len(string)):
		(a,) = unpack('B', string[i])
		tmp.append(a)
	result = Counter(tmp)
	return max(result, key=result.get)^32

def str_dec(string, key):
	tmp = []
	for i in xrange(len(string)):
		(a,) = unpack('B', string[i])
		tmp.append(chr(a ^ key))
	return ''.join(tmp)

if __name__ == '__main__':
	string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	key = find_key(string.decode('hex'))
	print "[+]key:",key
	print "[+]plaintext:",str_dec(string.decode('hex'), key)