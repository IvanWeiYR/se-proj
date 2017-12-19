import random
import os
import argparse

def generate(num_of_tc = 25, n = 5, max = 1001, dest = 'tc'):
	if not os.path.exists(dest):
		os.makedirs(dest)
	for i in range(num_of_tc):
		with open(dest + '/testcases_' + str(i) + '.txt', 'w') as f:
			testcase = []
			#if random_len:
			#	n = random.randint(1, 101)
			for j in range(n):
				val = random.randint(1, max)
				testcase.append(val)
			# if(i%5==0):
			# 	testcase.sort()
			origin_list_str = ",".join(str(x) for x in testcase)
			f.write(origin_list_str + '\n')
	print('Generated testcases.txt')


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Generate testcases for sorting algorithms')
	parser.add_argument('--ntc', default=25, type=int, help='number of testcases, default: 25')
	parser.add_argument('--len', default=5, type=int, help='length of list, default: 5')
	parser.add_argument('--max', default=1001, type=int, help='maximum value for each element in list, default: 1001')
	parser.add_argument('--dest', default='tc', type=str, help='destination folder to store the testcase .txt file, default: \'tc\'')

	args = parser.parse_args()
	generate(args.ntc, args.len, args.max, args.dest)
