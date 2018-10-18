#coding:utf-8
from hashlib import sha1
import multiprocessing
from itertools import permutations
import time

#字符集
charset = [('q','Q'),('w','W'),('5','%'),('8','('),('0','='),('i','I'),('+','*'),('n','N')]

#生成全部序号组合
def generate_index_list():
	number = [str(i) for i in range(len(charset))]
	index_list = [''.join(i) for i in permutations(number, len(charset))]
	return index_list

#生成全部上下键位组合，1代表上字符，0代表下字符
def generate_case_list():
	case_list = []
	for i in range(256):
		#要求上字符的数量大于等于2
		if bin(i).count('1') >= 2:
			case_list.append(bin(i)[2:].zfill(8))
	return case_list

#寻找密码
def try_and_calc(str_index, case_list):
	# 010101010
	for case in case_list:
		# 01234567
		res = ''
		for i in range(len(str_index)):
			res += charset[int(str_index[i])][int(case[int(i)])]
		if sha1(res).hexdigest() == "67ae1a64661ac8b4494666f58c4822408dd0a3e4":
			return res
			break

if __name__ == '__main__':
	start_time = time.time()
	case_list = generate_case_list()
	index_list = generate_index_list()
	#建立进程池
	pool = multiprocessing.Pool(processes=4)
	for index in index_list:
		res = pool.apply_async(try_and_calc, (index, case_list))
		#一旦返回结果，进程池终结
		if res.get():
			print "password:",res.get()
			pool.terminate()
			break
	pool.close()
	pool.join()
	print "Cost time:",time.time()-start_time