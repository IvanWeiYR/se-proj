def bubbleSort(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j]>alist[j+1]:
				temp = alist[j]
				alist[j] = alist[j+1]
				alist[j+1] = temp

#alist = [54,26,93,17,77,31,44,55,20]
#bubbleSort(alist)
#print(alist)