#coding:utf-8
import sys
from Crypto.Cipher import AES

BLOCKSIZE = 16

def strxor(a, b):
	""" xor two strings of different lengths """
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def strplus_one(s):# iv递增函数
	length=len(s)
	s_plus=ord(s[length-1])+1
	if s_plus<256:
		return s[:length-1]+chr(s_plus)
	else:
		return strplus_one(s[:length-1])+chr(0)

def ctr_decode(key,ciphertext):
	cipher = AES.new(key, AES.MODE_ECB)
	iv = ciphertext[:BLOCKSIZE]
	result = ''
	for i in range(1,len(ciphertext)/BLOCKSIZE):
		iv_enc = cipher.encrypt(iv)# 加密iv
		message = strxor(ciphertext[i*BLOCKSIZE:(i+1)*BLOCKSIZE],iv_enc)
		iv = strplus_one(iv)
		result += message
	if len(ciphertext) % BLOCKSIZE == 0:
		return result
	else:
		iv_enc = cipher.encrypt(iv)
		message = strxor(ciphertext[(len(ciphertext)/BLOCKSIZE)*BLOCKSIZE:],iv_enc)
		result += message
		return result

key='36f18357be4dbd77f050515c73fcf9f2'.decode('hex')
msg1='69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'.decode('hex')
msg2='770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'.decode('hex')
print ctr_decode(key,msg1)
print ctr_decode(key,msg2)