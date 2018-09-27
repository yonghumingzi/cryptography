from challenge3 import str_dec, find_key

def detect(string):
	for st in string:
		asc = ord(st)
		if not(65<=asc<=90 or 97<=asc<=122 or asc==32):
			return False
	return True

if __name__ == '__main__':
	file = open('4.txt', 'r')
	i = 0
	for line in file.readlines():
		i += 1
		line = line.strip()
		key = find_key(line.decode('hex'))
		result = str_dec(line.decode('hex'), key)
		if detect(result[:-1]):
			print "[+]line: ",i
			print "[+]plaintext: ",result
	file.close()