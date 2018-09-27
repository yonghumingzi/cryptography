from struct import unpack

def xor_key_enc(string, key):
	key_len = len(key)
	key_asc = []
	for i in xrange(key_len):
		(a,) = unpack('B', key[i])
		key_asc.append(a)
	out = []
	for i in xrange(len(string)):
		(a,) = unpack('B', string[i])
		out.append(chr(a ^ key_asc[i % len(key)]))
	return ''.join(out)

if __name__ == "__main__":
	text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
	key = "ICE"
	print xor_key_enc(text, key).encode('hex')
