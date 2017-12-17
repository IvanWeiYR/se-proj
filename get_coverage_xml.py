import cov
import copy
import time
from os import listdir
from os.path import isfile, join, basename, splitext

def start(module_name, func_name, testcases_folder = 'tc'):
	module = __import__(module_name)
	func = getattr(module, func_name)
	for f in [f for f in listdir(testcases_folder) if isfile(join(testcases_folder, f))]:
		if not f.endswith('.txt'):
			continue
		with open('tc/' + f) as file:
			line = file.readline()
			contents = line.split()
			origin_list = contents[0].split(',')
			sorted_list = contents[1].split(',')
			origin_list = list(map(int, origin_list))
			sorted_list = list(map(int, sorted_list))
			cov.begin()
			origin_list = func(origin_list)
			result = (origin_list == sorted_list)
			cov.end(result, module_name, splitext(basename(f))[0] + '.xml') 
	print('Generated coverage XML files at folder \'' + module_name + '\'')

if __name__ == '__main__':
	start('qsort', 'qsort')
