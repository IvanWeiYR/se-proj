import coverage
import xml.etree.ElementTree as ET
import os

cov = coverage.Coverage()

def begin():
	cov.start()

def end(isPass, program_name, folder = 'reports', report_name = 'coverage_with_result.xml'):
	cov.stop()
	cov.save()
	cov.xml_report(omit=['cov.py'])
	tree = ET.parse('coverage.xml')
	root = tree.getroot()
	result = ET.SubElement(root, 'result')
	result.set('pass', '0' if isPass else '1')
	result.tail = "\n"
	if not os.path.exists(folder):
		os.makedirs(folder)
	tree.write(folder + '/' + report_name, xml_declaration=True)