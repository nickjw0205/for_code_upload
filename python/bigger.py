def bigger(a,b):

	if a>b:
		return a
	else:
		return b

def biggest(a,b,c):
	return bigger(bigger(a,b),c)

def nedian(a,b,c):
	return bigger(biggest(a,b,c)
