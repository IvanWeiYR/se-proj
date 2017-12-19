import cov
import copy
import time
from os import listdir
from os.path import isfile, join, basename, splitext
import argparse

def start(module_name, func_name, testcases_folder = 'tc_sorting'):
	module = __import__(module_name)
	func = getattr(module, func_name)
	for f in [f for f in listdir(testcases_folder) if isfile(join(testcases_folder, f))]:
		if not f.endswith('.txt'):
			continue
		with open(testcases_folder + '/' + f) as file:
			line = file.readline()
			contents = line.split()
			origin_list = contents[0].split(',')
			origin_list = list(map(int, origin_list))
			cov.begin()
			sorted_list = func(origin_list)

			result = True
			if(len(origin_list) != len(sorted_list)):
				result = False
			else:
				for i in range(1,len(sorted_list)):
					if(sorted_list[i] < sorted_list[i-1]):
						result = False
						break
			cov.end(result, module_name, module_name, splitext(basename(f))[0]) 
	print('Generated coverage XML files at folder \'' + module_name + '\'')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Generate coverage .xml file from testcases for sorting algorithm')
	parser.add_argument('module', type=str, help='name of the module')
	parser.add_argument('func', type=str, help='name of entrance function')
	parser.add_argument('--src', default='tc_sorting', type=str, help='name of source folder containing testcase .txt files, default: \'tc\'')

	args = parser.parse_args()
	start(args.module, args.func, args.src)
