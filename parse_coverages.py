from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET

# folder: the name of folder contains coverage xml files
# program_name: the name of the python program, i.e. XXXX.py
def get_tests_matrix(folder, program_name):
	tests_matrix = [];

	for f in [f for f in listdir(folder) if isfile(join(folder, f))]:
		if not f.endswith('.xml'):
			continue
		test = []
		tree = ET.parse(folder + '/' + f)

		root = tree.getroot()
		for pkg in root.findall('.//package'):
			for clazz in pkg.findall('.//class[@filename="' + program_name + '"]'):
				for line in clazz.findall('.//line'):
					test.append(int(line.get('hits')))
		result = root.find('result').get('pass')
		test.append(int(result))
		tests_matrix.append(test)

	return tests_matrix

if __name__ == '__main__':
	get_tests_matrix('quickSort', 'quickSort.py')