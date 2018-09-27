#coding:utf-8
from collections import defaultdict

def compute_repeat(string):
	rep_res = defaultdict(lambda: -1)
	for i in range(0, len(string), 16): #分块
		block = string[i:i+16]
		rep_res[block] += 1
	return sum(rep_res.values()) #总重复数

if __name__ == '__main__':
	file = open('8.txt', 'r')
	max_repeat = 0
	enc_one = ''
	for line in file.readlines():
		cipher = line.strip()
		repeat = compute_repeat(cipher)
		if repeat >= max_repeat:
			max_repeat = repeat
			enc_one = cipher
	print enc_one
