import random
import string
import argparse
import os

#:;<=>?@
def gen_s1(n):
	N = n
	return ''.join(random.choice(":;<=>?@") for _ in range(N))

#[\]^_`
def gen_s2(n):
	N = n
	return ''.join(random.choice("[]^_`") for _ in range(N))

#{|}~
def gen_s3(n):
	N = n
	return ''.join(random.choice("{|}~") for _ in range(N))

def gen_upper(n):
	N = n
	return ''.join(random.choice(string.ascii_uppercase) for _ in range(N))

def gen_lower(n):
	N = n
	return ''.join(random.choice(string.ascii_lowercase) for _ in range(N))

def gen_digit(n):
	N = n
	return ''.join(random.choice(string.digits) for _ in range(N))



def gen_str(up,lo,num,s1,s2,s3):
	s = ""
	s = gen_upper(up) + gen_lower(lo) + gen_digit(num) + gen_s1(s1) + gen_s2(s2) + gen_s3(s3)
	return s

def generate(num_of_tc = 25, dest = 'tc_symbcount'):
	if not os.path.exists(dest):
		os.makedirs(dest)
	for i in range(num_of_tc):
		
		with open(dest + '/testcases_' + str(i) + '.txt', 'w') as f:
			# random gen
			up = random.randint(0,3)
			lo = random.randint(0,3)
			num = random.randint(0,3)
			s1 = random.randint(0,3)
			s2 = random.randint(0,3)
			s3 = random.randint(0,3)
			#s = gen_str(up,0,0,0,0,0)
			s = gen_str(up,lo,num,s1,s2,s3)
			#count_list = [up,0,0,0,0,0]
			count_list = [up,lo,num,s1,s2,s3]
			count_list_str = ",".join(str(x) for x in count_list)
			f.write(s + ' ' + count_list_str + '\n') 


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Generate testcases for sorting algorithms')
	parser.add_argument('--ntc', default=25, type=int, help='number of testcases, default: 25')
	parser.add_argument('--dest', default='tc_symbcount', type=str, help='destination folder to store the testcase .txt file, default: \'tc\'')

	args = parser.parse_args()
	generate(args.ntc, args.dest)