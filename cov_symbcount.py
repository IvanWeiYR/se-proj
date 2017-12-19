import cov
import copy
import time
from os import listdir
from os.path import isfile, join, basename, splitext
import argparse

def start(module_name, func_name, testcases_folder = 'tc_symbcount'):
	module = __import__(module_name)
	func = getattr(module, func_name)
	for f in [f for f in listdir(testcases_folder) if isfile(join(testcases_folder, f))]:
		if not f.endswith('.txt'):
			continue
		with open(testcases_folder + '/' + f) as file:
			line = file.readline()
			contents = line.split()
			inp = contents[0]
			out = contents[1].split(',')
			out = list(map(int, out))
			cov.erase()
			cov.begin()
			computed_list = func(inp)
			result = (computed_list == out)
			cov.end(result, module_name, module_name, splitext(basename(f))[0]) 
	print('Generated coverage XML files at folder \'' + module_name + '\'')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Generate coverage .xml file from testcases for sorting algorithm', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('module', type=str, help='name of the module')
	parser.add_argument('func', type=str, help='name of entry function')
	parser.add_argument('--src', default='tc_symbcount', type=str, help='name of source folder containing testcase .txt files')

	args = parser.parse_args()
	start(args.module, args.func, args.src)
