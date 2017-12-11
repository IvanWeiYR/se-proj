from random import *
from parse_coverages import get_tests_matrix

def genRandom():
	s,t = 3,2

	input = [[0 for x in range(s)] for y in range(t)]
	for x in range(0,t):
		for y in range(0,s):
			input[x][y] = randint(0,1)

	return input

def insertonSort(alist, index):
	rank = [len(alist) for x in range(c-1)]
	for i in range(len(alist)):
		key = alist[i]
		val = index[i]
		j = i - 1 
		while j >= 0 and alist[j] > key:
			alist[j+1] = alist[j]
			index[j+1] = index[j]
			j -= 1
		alist[j+1] = key
		index[j+1] = val

	ranking = len(alist)
	for i in range(len(alist)-1):
		ranking -= 1
		if alist[i] == alist[i+1]:
			rank[index[i+1]] = rank[index[i]]
		else:
			rank[index[i+1]] = ranking
	return rank

#get score
def getScore(test):
	
	#testCov = genRandom() 
	#testCov = [[1.0,1.0,0.0],[0.0,1.0,1.0],[1.0,0.0,0.0],[0.0,0.0,1.0]]
	
	testCov = test
	c = len(testCov[0]) #num of columns
	r = len(testCov) #num of rows
	hue = [0 for x in range(c-1)]
	sus = [0 for x in range(c-1)]
	#print(testCov)
	
	totalPassed = 0.0
	totalFailed = 0.0

	for x in range(r):
		if testCov[x][-1] == 0:
			totalPassed += 1
	totalFailed = r - totalPassed
	print('Total Passed: '+ str(totalPassed))
	print('Total Failed: '+ str(totalFailed))

	for x in range(c-1):
		passed = 0.0
		failed = 0.0
		for y in range(r):
			if testCov[y][x] == 1: #covered
				if testCov[y][c-1] == 0:#passed
					passed += 1
				else:#failed
					failed += 1
		testZero = passed*totalFailed+failed*totalPassed
		if passed == 0 and failed == 0 or totalFailed == 0:
			hue[x] = 1.0
			sus[x] = 0.0
		elif testZero == 0 or totalPassed == 0:
			hue[x] = 0.0
			sus[x] = 1.0
		else:
			hue[x] = (passed/totalPassed)/(passed/totalPassed+failed/totalFailed)
			sus[x] = 1.0 - hue[x]


	return sus,hue


# test = [
#     [1,1,1,1,0,1,1,0,0,0,0,0,1,0],
#     [1,1,1,1,1,0,0,0,0,0,0,0,1,0],
#     [1,1,1,0,0,0,0,1,1,1,0,0,1,0],
#     [1,1,1,0,0,0,0,1,1,0,1,0,1,0],
#     [1,1,1,1,0,1,0,0,0,0,0,0,1,0],
#     [1,1,1,1,0,1,1,0,0,0,0,0,1,1],
#     ]

test = get_tests_matrix('qsort', 'qsort.py')
c = len(test[0])
sus,hue = getScore(test)
index = [x for x in range(c-1)]


sorted_list = list(sus)
print(sorted_list)
rank = insertonSort(sorted_list,index)
# for x in range(c-1,0,-1):
# 	print("x is :",x)
# 	if x > 0:
# 		if sorted[x-1] == sorted[x-2]:
# 			rank[x-2] = rank[x-1]

#rank will record index of the corresponding value in sorted

#indexes corresponding to statement no.
print("rank is :",rank)