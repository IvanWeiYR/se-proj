import random
def generate(folder_name = 'tc'):
	for i in range(1000):
		with open(folder_name + '/testcases_' + str(i) + '.txt', 'w') as f:
			testcase = []
			#n = random.randint(1, 101)
			n = 25
			for j in range(n):
				val = random.randint(1, 1001)
				testcase.append(val)
			origin_list_str = ",".join(str(x) for x in testcase)
			testcase.sort()
			sorted_list_str = ",".join(str(x) for x in testcase)
			f.write(origin_list_str + ' ' + sorted_list_str + '\n')
	print('Generated testcases.txt')


if __name__ == "__main__":
	generate()
