from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET

def get_tests_matrix(folder, program_name):
	tests_matrix = [];

	for f in [f for f in listdir(folder) if isfile(join(folder, f))]:
		print(f)
		if not f.endswith('.xml'):
			continue
		test = []
		tree = ET.parse(folder + '/' + f)


		root = tree.getroot()
		for pkg in root.findall('.//package'):
		    print(pkg.tag)
		    for clazz in pkg.findall('.//class[@filename="' + program_name + '"]'):
		        print(clazz.tag)
		        for line in clazz.findall('.//line'):
		            print('line ' + line.get('number') + ' : ' + line.get('hits'))
		            test.append(int(line.get('hits')))
		result = root.find('result').get('pass')
		test.append(int(result))
		tests_matrix.append(test)
		print('result: ' + result)

	print(tests_matrix)
	return tests_matrix

if __name__ == '__main__':
	#get_tests_matrix('bubbleSort', 'bubbleSort.py')
	get_tests_matrix('quickSort', 'quickSort.py')