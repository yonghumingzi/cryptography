#coding:utf-8
import sys
from Crypto.Cipher import AES
from Crypto import Random

BLOCKSIZE=16

def strxor(a, b):
	""" xor two strings of different lengths """
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def encry_CBC_AES(key,message):
	""" AES encryption in CBC mode """
	pad=BLOCKSIZE-len(message)%BLOCKSIZE #padding
	for dummy_idx in range(pad):
		m=m+chr(pad)
	cipher = AES.new(key, AES.MODE_ECB)
	iv = Random.new().read(BLOCKSIZE)
	result=iv
	for idx in range(len(message)/BLOCKSIZE):
		ciphertext=cipher.encrypt(strxor(message[idx*BLOCKSIZE:(idx+1)*BLOCKSIZE],iv))
		iv=ciphertext
		result+=ciphertext
	return result

def decry_CBC_AES(key,ciphertext):
	""" AES decryption in CBC mode """
	cipher = AES.new(key, AES.MODE_ECB)
	iv = ciphertext[:BLOCKSIZE] #密文的第一块，作为新的iv
	result=''
	for idx in range(1,len(ciphertext)/BLOCKSIZE): #对于每一块
		message=strxor(cipher.decrypt(ciphertext[idx*BLOCKSIZE:(idx+1)*BLOCKSIZE]),iv)
		iv=ciphertext[idx*BLOCKSIZE:(idx+1)*BLOCKSIZE] #更新iV
		result+=message
	pad=len(result)
	return result[:pad-ord(result[pad-1])] # 去除填充，result[pad-1]对应要去除的数目


key='36f18357be4dbd77f050515c73fcf9f2'.decode('hex')
mes = "It couldn't be easier to renew your car insurance cover with 123"
c = encry_CBC_AES(key, mes)
print len(c)
print len(mes)
d = decry_CBC_AES(key, c)
print d