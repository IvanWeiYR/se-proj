from random import *

def genRandom():
	s,t = 3,2

	input = [[0 for x in range(s)] for y in range(t)]
	for x in range(0,t):
		for y in range(0,s):
			input[x][y] = randint(0,1)

	return input

#quick sort
def quickSort(alist,rank):
	quickSortSplit(alist,0,len(alist)-1,rank)

def quickSortSplit(alist,first,last,rank):
	if first < last:
		splitPoint = partition(alist,first,last,rank)

		quickSortSplit(alist,first,splitPoint - 1,rank)
		quickSortSplit(alist,splitPoint + 1, last,rank)

def partition(alist, first, last,rank):
	
	pivot = alist[first]		

	left = first + 1
	right = last

	done = False

	while not done:

		while left <= right and alist[left] <= pivot:
			left = left + 1

		while alist[right] >= pivot and right >= left:
			right = right - 1

		if right < left:
			done = True
		else:
			temp = alist[left]
			alist[left] = alist[right]
			alist[right] = temp

			temp1 = rank[left]
			rank[left] = rank[right]
			rank[right] = temp1


	temp = alist[first]
	alist[first] = alist[right]
	alist[right] = temp

	temp1 = rank[first]
	rank[first] = rank[right]
	rank[right] = temp1

	return right


#get score
def getScore(test):
	
	#testCov = genRandom() 
	#testCov = [[1.0,1.0,0.0],[0.0,1.0,1.0],[1.0,0.0,0.0],[0.0,0.0,1.0]]
	
	testCov = test
   	s = len(testCov[0])
   	t = len(testCov)
	hue = [0 for x in range(s)]
	sus = [0 for x in range(s)]
	#print(testCov)
	
	totalPassed = 0.0
	totalFailed = 0.0

	for x in range(t):
		if testCov[x][s-1] == 0.0:
			totalPassed += 1
	totalFailed = t - totalPassed

	for x in range(s):
		passed = 0.0
		failed = 0.0
		for y in range(t):
			if testCov[y][x] == 1 and testCov[y][s-1] == 0:
				passed +=1
			if testCov[y][x] == 1 and testCov[y][s-1] == 1:
				failed +=1
		testZero = passed*totalFailed+failed*totalPassed
		if 	totalPassed == 0 or totalFailed == 0 or testZero == 0:
			hue[x] = 0
			sus[x] = 1
		else:
			hue[x] = (passed/totalPassed)/(passed/totalPassed+failed/totalFailed)
			sus[x] = 1 - hue[x]


	return sus,hue


test = [
    [1,1,1,1,0,1,1,0,0,0,0,0,1,0],
    [1,1,1,1,1,0,0,0,0,0,0,0,1,0],
    [1,1,1,0,0,0,0,1,1,1,0,0,1,0],
    [1,1,1,0,0,0,0,1,1,0,1,0,1,0],
    [1,1,1,1,0,1,0,0,0,0,0,0,1,0],
    [1,1,1,1,0,1,1,0,0,0,0,0,1,1],
    ]
s = len(test[0])
sus,hue = getScore(test)
rank = [x for x in range(s)]


sorted = list(sus)
quickSort(sorted,rank)

#rank will record index of the corresponding value in sorted
print sus
print sorted
print rank
