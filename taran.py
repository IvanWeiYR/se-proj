from random import randint

def main():
	a = randint(0,9)
	b = randint(0,9)
	c = max(a,b)
	print c
	if c > 5 & c <9:
		print "yes"
	else: 
		print "no"
		print "shit"
		print "yea"

def max(a,b):
	if a>b:
		return a
	else:
		return b


main()