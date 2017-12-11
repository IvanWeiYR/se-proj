def quickSort(alist):
	quickSortSplit(alist,0,len(alist)-1)
	return alist

def quickSortSplit(alist,first,last):
	if first < last:
		splitPoint = partition(alist,first,last)

		quickSortSplit(alist,first,splitPoint - 1)
		quickSortSplit(alist,splitPoint + 1, last)
	else:
		return alist

def partition(alist, first, last):
	
	pivot = alist[last]		

	left = first
	right = last - 1

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
			alist[right] = alist[left]
			alist[left] = temp

	temp = alist[last]
	alist[last] = alist[left]
	alist[left] = temp

	return left

#alist = [54,26,93,17,77,31,44,55,20]
#quickSort(alist)
#print(alist)

if __name__ == "__main__":
	x = [3,4,5,1,2,8,3,7,6]
	print(x)
	print(quickSort(x))