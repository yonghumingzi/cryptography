#coding=utf-8
from __future__ import division
from struct import unpack
from challenge3 import find_key, str_dec
from challenge5 import xor_key_enc

def str_xor(str1, str2):#异或字符串
	result = []
	for i in xrange(len(str1)):
		(a,), (b,) = unpack('B', str1[i]), unpack('B', str2[i])
		result.append(bin(a ^ b))
	return result

def compute_hamming(str1, str2):
	if len(str1) > len(str2): #补齐
		str2 = '%s%s' % (str2, '\x00' * (len(str1) - len(str2)))
	elif len(str2) > len(str1):
		str1 = '%s%s' % (str1, '\x00' * (len(str2) - len(str1)))
	out = str_xor(str1, str2)
	distance = 0
	for o in out:
		distance += o.count('1') #汉明距离
	return distance

def find_key_length():
	cipher = "".join(list(open("6.txt", "r"))).decode("base64")
	max_length = 40
	if len(cipher) < max_length:
		max_length = len(cipher)
	res_length = 0
	result = {}
	for key_length in range(2, max_length+1):
		for i in range(0, 13, 2):#第二位反复尝试，为29
			dis_list = []
			block_1 = cipher[key_length*i:key_length*(i+1)]
			block_2 = cipher[key_length*(i+1):key_length*(i+2)]
			dis_list.append(compute_hamming(block_1,block_2)/key_length)
			distance = sum(dis_list)/len(dis_list)
			result[key_length] = distance
	return min(result, key=result.get)

def transpose_blocks(cipher, key_length):
	cipher += '\x00' * (key_length - len(cipher) % key_length)#补齐
	blocks = []
	for i in range(0, len(cipher), key_length):
		blocks.append(cipher[i:i+key_length])
	transposed_blocks = []
	for i in range(key_length):
		transposed_blocks.append('') 
		for block in blocks:
			transposed_blocks[i] += block[i]
	return transposed_blocks

def find_the_key(blocks):
	result = ''
	for block in blocks:
		key = find_key(block)
		result += chr(key)
	return result

if __name__ == '__main__':
	cipher = "".join(list(open("6.txt", "r"))).decode("base64")
	key_length = find_key_length()
	blocks = transpose_blocks(cipher, key_length)
	key = find_the_key(blocks)
	print "[+]key: ",key
	print "plaintext: "
	print xor_key_enc(cipher, key)