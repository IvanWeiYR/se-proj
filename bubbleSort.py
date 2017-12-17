def bubbleSort(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j]>alist[j+1]:
				temp = alist[j]
				alist[j] = alist[j+1]
				alist[j+1] = temp
	return alist

if __name__ == "__main__":
	x = [3,4,5,1,2,8,3,7,6]
	print(x)
	print(bubbleSort(x))

