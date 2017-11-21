from sum import sum
import cov
from quickSort import quickSort
from bubbleSort import bubbleSort
import copy
import time

test_cases = [
	[54,26,93,17,77,31,44,55,20],
	[2,3,35,56,6,23,5,100,5,2,-1], 
	[45,2,3,50,48,1020,46,23,3,92,1], 
	[2738,5432,67,4,5764,3,23,6,7,35,22,22],
	[1,2,3,4,5,6,7]
]

def start():
	prefix = 'bubbleSort'
	for tc in test_cases:
		
		copied_tc = copy.deepcopy(tc)

		#quickSort(copied_tc)
		bubbleSort(copied_tc)
		tc.sort()
		cov.begin()
		result = (copied_tc == tc)
		cov.end(result, prefix, prefix + '_' + str(int(round(time.time() * 1000))) + '.xml') 

if __name__ == '__main__':
	start()
