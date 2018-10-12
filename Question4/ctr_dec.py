import sys
from Crypto.Cipher import AES
from Crypto import Random

BLOCKSIZE = 16

def strxor(a, b):
	""" xor two strings of different lengths """
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def strplus_one(s):
	"""plus one to input string and return a string. Used to increase iv."""
	length=len(s)
	s_plus=ord(s[length-1])+1
	if s_plus<256:
		return s[:length-1]+chr(s_plus)
	else:
		return strplus_one(s[:length-1])+chr(0)

def encry_CTR_AES(key,message):
	""" AES encryption in CTR mode """
	cipher = AES.new(key, AES.MODE_ECB)
	iv = Random.new().read(BLOCKSIZE)
	result=iv
	for idx in range(len(message)/BLOCKSIZE):
		iv_enc=cipher.encrypt(iv)
		ciphertext=strxor(message[idx*BLOCKSIZE:(idx+1)*BLOCKSIZE],iv_enc)
		iv=strplus_one(iv)
		result+=ciphertext
	if len(message)%BLOCKSIZE==0:
		return result
	else:
		iv_enc=cipher.encrypt(iv)
		ciphertext=strxor(message[(len(message)/BLOCKSIZE)*BLOCKSIZE:],iv_enc)
		result+=ciphertext
		return result

def decry_CTR_AES(key,ciphertext):
	""" AES decryption in CTR mode """
	cipher = AES.new(key, AES.MODE_ECB)
	iv = ciphertext[:BLOCKSIZE]
	result=''
	for idx in range(1,len(ciphertext)/BLOCKSIZE):
		iv_enc=cipher.encrypt(iv)
		message=strxor(ciphertext[idx*BLOCKSIZE:(idx+1)*BLOCKSIZE],iv_enc)
		iv=strplus_one(iv)
		result+=message
	if len(ciphertext)%BLOCKSIZE==0:
		return result
	else:
		iv_enc=cipher.encrypt(iv)
		message=strxor(ciphertext[(len(ciphertext)/BLOCKSIZE)*BLOCKSIZE:],iv_enc)
		result+=message
		return result

key='36f18357be4dbd77f050515c73fcf9f2'.decode('hex')
m = "It couldn't be easier to renew your car insurance cover with 123"
c = encry_CTR_AES(key, m)
print len(c)
print len(m)
d = decry_CTR_AES(key, c)
print d