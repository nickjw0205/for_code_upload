def minsteps0(n):
	if n > 1:
		r = 1 + minsteps0(n-1)
		if n % 2 == 0:
			r = min(r,1+minsteps0(n//2))
		if n % 3 ==0:
			r = min(r,1 + minsteps0(n//3))
			return r 
	else:
		return 0

def minsteps1(n):
	memo = [0] * (n + 1)
	def loop(n):
		if n > 1:
			if memo[n] != 0:
				return memo[n]
			else:
				memo[n] = 1 + loop(n-1)
				if n % 2 == 0:
					memo[n] = min(memo[n],1 + loop(n//2))
				if n % 3 == 0:
					memo[n] = min(memo[n],1 + loop(n//3))
				return memo[n]
		else:
			return 0
	return loop(n)



def minsteps(n):
	memo = [0] * (n+1)
	for i in range(n+1):
		if i > 1:
			memo[i] = 1 + memo[i-1]
			if i % 2 == 0:
				memo[i] = min(memo[i],1 + memo[i//2])
			if i % 3 == 0:
				memo[i] = min(memo[i],1 + memo[i//3])
		else:
			memo[i] = 0
	return memo[n]

# print("minsteps(1) :",minsteps(1))
# print("minsteps(2) :",minsteps(2))
# print("minsteps(3) :",minsteps(3))
# print("minsteps(4) :",minsteps(4))
# print("minsteps(7) :",minsteps(7))
# print("minsteps(10) :",minsteps(10))
# print("minsteps(23) :",minsteps(23))
# print("minsteps(237) :",minsteps(237))
# print("minsteps(317) :",minsteps(317))
# print("minsteps(514) :",minsteps(514))
# print("minsteps(997) :",minsteps(997))
# print("minsteps(998) :",minsteps(998))

def gugudan1():
	for k in range(2,10):
		for j in range(2,10):
			if j % 5 == 0:
				print(k," x ",j,"=",str(k*j).rjust(2))
			else:
				print(k," x ",j,"=",str(k*j).rjust(2),end="  ")
		print()
		print()
def gugudan2():
	for k in [2,6]:
		for i in range(2,10):
			for j in range(k,k+4):
				print(j,"x",i,"=",str(i*j).rjust(2),end="  ")
			print()
		print()

t = input("Type of Gugudan[Horizontal, Vertical]:")
print()
if(t == "Horizontal"):
	gugudan1()
elif(t == "Vertical"):
	gugudan2()
else:
	print("Neither horizontal of vertical")