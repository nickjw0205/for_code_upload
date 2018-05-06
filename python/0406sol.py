def insert0(x,ss): 
	if ss != []: 
		if x <= ss[0]: 
			return [x] + ss
		else: 
			return [ss[0]]+insert0(x,ss[1:])
	else: 
		return [x]

def insert1(x,ss):
	def loop(ss,left):
		if ss != []:
			if x <= ss[0]:
				return [x] + ss
			else:
				return [ss[0]]+insert(x,ss[1:])
		else:
			return [x]
	return loop(ss,[])

def insert(x,ss):
	left = []
	while ss != []:
		if x <= ss[0]:
			return left + [x] + ss
		else:
			left, ss =  left + [ss[0]], ss[1:] 
	return left + [x]

def isort0(s):
	if s !=[]:
		return insert(s[0],isort0(s[1:]))
	else:
		return[]

def isort1(s):
	def loop(s,ss):
		if s !=[]:
			return loop(s[1:],insert(s[0],ss))
		else:
			return ss
	return loop(s,[])

def isort(s):
	ss = []
	while s != []:
		s,ss = s[1:], insert(s[0],ss)
	return ss
#실습6 isort를 for문으로 바꾸기
def isortfor(s):
	ss = []
	for i in range(0,len(s)):
		ss = insert(s[i],ss)
	return ss

#실습7
def merge1(left,right):
	ss = []
	def loop(left,right,ss):
		if not (left == [] or right == []):
			if left[0] <= right[0]:
				ss.append(left[0])
				return loop(left[1:],right,ss)
			else:
				ss.append(right[0])
				return loop(left,right[1:],ss)
		else:
			return ss + left + right
	return loop(left,right,ss)

def merge(left,right): 
	ss = [] 
	while not (left == [] or right == []): 
		if left[0] <= right[0]: 
			ss.append(left[0])
			left, right = left[1:], right
		else: 
			ss.append(right[0])
			left, right = left, right[1:]
	return ss + left + right

def bsort(s):
	for k in range(len(s)-1):
		for i in range(0,len(s)-1):
			if s[i] > s[i+1]:
				s[i], s[i+1] = s[i+1],s[i]
	return s

x = 4
ss = [1,3,6,7]
s = [4,7,2,5,9,1]
left = [1,4,5,8]
right = [2,3,6,9]

print("insert0(x,ss)",insert0(x,ss))
print("insert1(x,ss)",insert1(x,ss))
print("insert(x,ss)",insert(x,ss))
print("isort1(s)",isort1(s))
print("isort(s)",isort(s))
print("isortfor(s)",isortfor(s))
print("merge1(left,right)",merge1(left,right))
print("merge(left,right)",merge(left,right))
print("bsort(s)",bsort(s))









