def insertionSort(alist):
	for i in range(len(alist) -1):
		key = alist[i]
		j = i - 1 
		while j >= 0 and alist[j] > key:
			alist[j+1] = alist[j]
			j -= 1
		alist[j+1] = key
	return alist