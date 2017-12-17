import coverage
import xml.etree.ElementTree as ET
import os

cov = coverage.Coverage()

def erase():
	cov.erase()

def begin():
	cov.start()

def end(isPass, program_name, folder = 'reports', report_name = 'coverage_with_result'):
	cov.stop()
	cov.save()
	cov.xml_report(outfile=report_name+'.xml', omit=['cov.py'])
	tree = ET.parse(report_name+'.xml')
	root = tree.getroot()
	result = ET.SubElement(root, 'result')
	result.set('pass', '0' if isPass else '1')
	result.tail = "\n"
	if not os.path.exists(folder):
		os.makedirs(folder)
	tree.write(folder + '/' + report_name+'.xml', xml_declaration=True)
	#print(root.text)
	os.remove(report_name+'.xml')