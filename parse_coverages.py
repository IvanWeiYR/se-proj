from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET

# folder: the name of folder contains coverage xml files
# program_name: the name of the python program, i.e. XXXX for XXXX.py
def get_tests_matrix(folder, program_name):
	tests_matrix = []

	for f in [f for f in listdir(folder) if isfile(join(folder, f))]:
		if not f.endswith('.xml'):
			continue
		test = []
		tree = ET.parse(folder + '/' + f)

		root = tree.getroot()
		for pkg in root.findall('.//package'):
			for clazz in pkg.findall('.//class[@filename="' + program_name + '.py"]'):
				lines = clazz.findall('.//line')
				max_line = int(lines[-1].get('number'))
				test = [0] * (max_line + 1)
				for line in lines:
					test[int(line.get('number')) - 1] = int(line.get('hits'))
		result = root.find('result').get('pass')
		test[-1] = int(result)
		print('-----')
		print(f)
		# alist = [x for x in range(44)]
		# print(alist)
		print(test)
		print(len(test))
		tests_matrix.append(test)

	return tests_matrix

if __name__ == '__main__':
	m = get_tests_matrix('count', 'count')
	#print(m)