#coding:utf-8
import hashlib
from base64 import b64decode
from Crypto.Cipher import AES
from question1_2 import strxor

def parity_check(string):# 奇偶校验
	Kenc = ''
	for i in range(0,len(string),2):
		number = bin(int(string[i:i+2],16)).count("1")#求出
		if number % 2 == 0:
			Kenc += hex(int(string[i:i+2],16) ^ 1)[2:]
		else:
			Kenc += string[i:i+2]
	return Kenc

def cbcDecrypt1(key, cypherText):# 全0初始化向量下的CBC解密
    k = key.decode('hex')
    ct = cypherText.decode('hex')
    iv = "00000000000000000000000000000000".decode('hex')
    obj = AES.new(k,AES.MODE_CBC,iv)
    paddedStr = obj.decrypt(ct)
    # 去填充
    if paddedStr[-1] == "\x01":
    	return paddedStr[:-1]
    elif paddedStr[-1] == "\x00":
    	for i in range(2,17):
    		if paddedStr[-i] == "\x01":
    			return paddedStr[:-i]
    	return False
    else:
    	return False
    #return paddedStr[:-7]

if __name__ == '__main__':
	enc_msg = "9MgYwmuPrjiecPMx61O6zIuy3MtIXQQ0E59T3xB6u0Gyf1gYs2i3K9Jxaa0zj4gTMazJuApwd6+jdyeI5iGHvhQyDHGVlAuYTgJrbFDrfB22Fpil2NfNnWFBTXyf7SDI"
	p = "12345678<811101821111167"
	#SHA-1后取前32位
	p = hashlib.sha1(p).hexdigest()[:32]
	c = "00000001"
	p = p+c
	#SHA-1后取前32位
	K = hashlib.sha1(p.decode('hex')).hexdigest()[:32]
	#奇偶校验
	K = parity_check(K[:32])
	#K：ea8645d97ff725a898942aa280c43179
	result = cbcDecrypt1(K, b64decode(enc_msg).encode('hex'))
	print result