def count(alist):
	length = len(alist)
	i = length-1	
	letter = 0
	num = 0
	while(i>=0):
		s = alist[i]
		if ord('A') <= ord(s) and ord('Z') >= ord(s): 
			upperLetter += 1
		elif ord('a') <= ord(s) and ord('z') >= ord(s):
			lowerLetter += 1
		elif ord('0') <= ord(s) and ord('9') >= ord(s):
			num += 2
		elif ord(':') <= ord(s) and ord('@') >= ord(s):#58~64
			special1 += 1
		elif ord('[') <= ord(s) and ord('`') >= ord(s):#91~96
			special2 += 1
		elif ord('{') <= ord(s) and ord('~') >= ord(s):#123~126
			special3 += 1
		i -= 1
	return [upperLetter,lowerLetter,num,special1,special2,special3]
def main():
	alist = "abcGsdaGH46346"
	print(count(alist))

#main()