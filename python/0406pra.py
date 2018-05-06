def ssort2(s):
	def loop(s,ss):
		if s !=[]:
			smallest = min(s)
			s.remove(smallest)
			ss.append(smallest)
			return loop(s,ss)
		else:
			return ss
	return loop(s,[])

def ssort3(s):
	ss = []
	while s !=[]:
		smallest = min(s)
		s.remove(smallest)
		ss.append(smallest)
	return ss

def ssort(s):
	if s !=[]:
		smallest = min(s)
		s.remove(smallest)
		return [smallest] + ssort(s)
	else:
		return []


def ssort4(s):
	ss=[]
	for _ in range(len(s)):
		smallest=min(s)
		s.remove(smallest)
		ss.append(smallest)
	return ss

def isort0(s):
	if s !=[]:
		return insert(s[0],isort0(s[1:]))
	else:
		return []


def insert(x,ss):
	if ss !=[]:
		if x<=ss[0]:
			ss = x+ss
		if x>=ss[0]:
			return s[0]+s[1:]

def msort(s):
	if len(s)>1:
		mid = len(s) // 2
		return merge(msort(s[:mid]),msort(s[mid:]))
	else:
		return s




def merge(left,right):
	if not (left == [] or right == [] ):
		if left[0] <= right[0]:
			return [left[0]] + merge(left[1:],right)
		else:
			return[right[0]]+merge0(left,right[1:])
	else:
		return left + right

print(isort0([125435,4352,23123,2123,5647,12,6433,654376453,123,124214]))

#-----------필기--------------#
#필기 mutable:list
#.   immutable:string
#list = list2
#이경우 list2를 수정할경우 list도 변경되나 list2 = list[:]로 하면 list2를 건드려도 list는 바뀌지 않음
#list2[2:4] = [5777] 이경우 리스트2함수의 3번째4번째 값이 합쳐지면서 5777으로 바끼게ㅐ 된다
# range라는 시퀀스 정수의 범위를 나타냄 --> range[1,10] ---->1~9
#확인해보는방법은 3 in range 로 트루와 폴스를 확인한다.  그럼 range(10)=? ----->그럼 무조건 (0,10)으로 인식
#range(1,10,3)---->1부터9까지 3씩 증가하는 수열을 만들어라 1,4,7
# r = range(10,-8,-3) 10,7,4,1,-2,-5
#basis = [] /// induction = > L=> [x]+L



