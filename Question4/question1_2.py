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

def cbc_decode(key, ciphertext):
	cipher = AES.new(key, AES.MODE_ECB)
	iv = ciphertext[:BLOCKSIZE] #密文的第一块，作为新的iv
	result = ''
	for i in range(1,len(ciphertext)/BLOCKSIZE): #对于每一块
		message=strxor(cipher.decrypt(ciphertext[i*BLOCKSIZE:(i+1)*BLOCKSIZE]),iv)
		iv=ciphertext[i*BLOCKSIZE:(i+1)*BLOCKSIZE] #更新iV
		result+=message
	pad = len(result)
	return result[:pad-ord(result[pad-1])]  #去除填充，result[pad-1]对应要去除的数目

if __name__ == '__main__':
	key='140b41b22a29beb4061bda66b6747e14'.decode('hex')
	msg1='4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'.decode('hex')
	msg2='5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'.decode('hex')
	print cbc_decode(key,msg1)
	print cbc_decode(key,msg2)