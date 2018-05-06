import time
def countdown(n):
	while n>0:
		print(n)
		time.sleep(1)
		n = n-1 
	print("발사!")

def sigma(n):
	def loop(n,acc):
		if n > 0:
			return loop(n-1,n+acc)
		else:
			return acc
	return loop(n,0)

def sigma(n):
	acc = 0
	while n > 0:
		acc = n + acc
		n = n-1
	return acc

def power(b,n):
	def loop(b,n,acc)
		if n >0:
			return loop(b,n-1,acc*b)
		else:
			return acc
	return loop(b,n,1)

def power(b,n):
	acc = 1
	while n >0:
		b,n,acc = b,n-1,acc*b
	return acc

def fastpower(b,n):
	def loop(b,n,acc):
		if n>0:
			if n%2==0:
				return loop(b**2,n//2,acc) 
		else:
			return loop (b,n-1,b*acc)
	else:
		return prod
return loop(b,n,1)


print(countdown(600))














