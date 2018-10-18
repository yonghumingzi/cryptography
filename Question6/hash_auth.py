#coding:utf-8
import os
from Crypto.Hash import SHA256

def calc_hash(file, block_size):
	#获取文件大小
	file_size = os.path.getsize(file)
	#求最后一块大小
	last_size = file_size % block_size
	#总块数
	block_num = file_size / block_size
	#读出文件内容
	fp = open(file, 'rb')
	content = fp.read()
	#求最后一块的hash
	sha256 = SHA256.new()
	sha256.update(content[file_size-last_size:file_size])
	hash_0 = sha256.digest()
	#提取并反序
	blocks = []
	for i in range(block_num):
		blocks.append(content[i*block_size:(i+1)*block_size])
	blocks = blocks[::-1]
	#求出h0
	for block in blocks:
		sha256 = SHA256.new()
		sha256.update(block + hash_0)
		hash_0 = sha256.digest()
	fp.close()
	return hash_0.encode('hex')

if __name__ == '__main__':
	block_size = 1024
	file_verify = "6.2_check.mp4"
	file_verify_h0 = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"
	my_h0 = calc_hash(file_verify, block_size)
	#验证6.2
	print "hash_0 of the video 6.2:",my_h0
	if my_h0 == file_verify_h0:
		print "video 6.2 authentication success!"
	#验证6.1
	file_1_origin = "6.1_origin.mp4"
	file_1_check = "6.1_check.mp4"
	origin_h0 = calc_hash(file_1_origin, block_size)
	print "hash_0 of the orignal video 6.1:",origin_h0
	check_h0 = calc_hash(file_1_check, block_size)
	print "hash_0 of the checked video 6.1:",check_h0
	if check_h0 == origin_h0:
		print "video 6.1 authentication success!"