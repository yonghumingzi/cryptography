#coding:utf-8
from __future__ import division
import collections
from struct import unpack

def readFile():
	file = open('ciphertext.txt','r')
	cont = file.read()
	cipher_len = len(cont)
	i = 0
	cipher = []
	while i < cipher_len:
		cipher.append(cont[i:i+2])
		i+=2
	file.close()
	return cipher

def findKeyLength(cipher):#key_length = 7
	max_key_length = 13
	min_key_length = 2
	key_space = 256
	now_length = 2
	while min_key_length <= now_length and now_length <= max_key_length:
		print "[+]now_length: ", now_length
		for i in range(now_length):
			list = cipher[i::now_length]
			IC = calculate_IC(list)
			print "[+]IC: ",IC
		now_length += 1

def calculate_IC(cipher):
	result = 0
	length = len(cipher)
	cipher_dict = collections.Counter(cipher)
	for key in cipher_dict.keys():
		result += (cipher_dict[key]*(cipher_dict[key]-1))/(length*(length-1))
	return result

def find_key(cipher, key_length = 7):
	tmp = []
	key = []
	for i in xrange(len(cipher)):
		tmp.append(int(cipher[i],16))
	#tmp: ascii
	for pos in xrange(key_length):
		text = tmp[pos::key_length]
		for i in xrange(1,256):
			flag = 0
			for t in text:
				if not_readable(i ^ t):#一旦发现不可读、跳出
					flag = 1
					break
			if flag == 1:#尝试下一个i
				continue
			else:
				key.append(i)
	return key

def not_readable(asc):
    if asc not in range(48,58)+range(97,123)+range(65,91)+[32,44,46]:
        return True
    else:
        return False

def decode_cipher(cipher, key):
	tmp = []
	result = []
	for i in xrange(len(cipher)):
		tmp.append(int(cipher[i],16))
	for i in xrange(len(cipher)):
		result.append(chr(tmp[i] ^ key[i % 7]))
	return ''.join(result)

if __name__ == "__main__":
	cipher = readFile()

	key = find_key(cipher)
	print "key: ",key
	print "plaintext: "
	print decode_cipher(cipher, key)
