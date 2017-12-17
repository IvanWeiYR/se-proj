def count(alist):
	length = len(alist)
	i = length-1	
	letter = 0
	num = 0
	while(i>=0):
		s = alist[i]
		if ord('A') <= ord(s) and ord('Z') >= ord(s): 
			letter += 2
		if ord('a') <= ord(s) and ord('z') >= ord(s):
			letter += 1
		if ord('0') <= ord(s) and ord('9') >= ord(s):
			num += 2
		i -= 1
	return [letter,num]
def main():
	alist = "abcGsdaGH46346"
	print(count(alist))

#main()