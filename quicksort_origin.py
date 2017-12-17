def partition(alist, low, high):
	pivot = alist[high]
	i = low - 1
	for j in range(low, high):
		if alist[j] <= pivot:
			i += 1
			temp = alist[i]
			alist[i] = alist[j]
			alist[j] = temp
	temp = alist[i+1]
	alist[i+1] = alist[high]
	alist[high] = temp
	return i+1
def quicksort(alist, low, high):
	if low <= high:
		pivot = partition(alist, low, high)
		quicksort(alist, low, pivot-1)
		quicksort(alist, pivot+1, high)
def sort(alist):
	quicksort(alist, 0, len(alist)-1)
	return alist

if __name__ == '__main__':
	arr = [3,4,5,1,2,8,3,7,6]
	print(arr)
	print(sort(arr))
	print(arr)