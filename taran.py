from random import *

def genRandom():
	s,t = 3,2

	input = [[0 for x in range(s)] for y in range(t)]
	for x in range(0,t):
		for y in range(0,s):
			input[x][y] = randint(0,1)

	return input
def main():
	s,t = 3,2
	hue = [0 for x in range(s)]
	testCov = genRandom()
	print(testCov)
	
	totalPassed = 0
	totalFailed = 0 

	for x in range(t):
		if testCov[x][s-1] == 0:
			totalPassed += 1
	totalFailed = t - totalPassed

	for x in range(s):
		passed = 0
		failed = 0
		for y in range(t):
			if testCov[y][x] == 1 and testCov[y][s-1] == 0:
				passed +=1
			if testCov[y][x] == 1 and testCov[y][s-1] == 1:
				failed +=1
		testZero = passed*totalFailed+failed*totalPassed
		if 	totalPassed == 0 or totalFailed == 0 or testZero == 0:
			hue[x] = 0
		else:
			hue[x] = (passed/totalPassed)/(passed/totalPassed+failed/totalFailed)
	return hue

hueArr = main()
print(hueArr)


