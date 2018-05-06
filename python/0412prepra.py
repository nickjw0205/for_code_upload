#import random
#db = random.sample(range(10000),1000)
#key = data[109]
#print(db.index(key))


# import random
# kk = random.sample(range(100),20)
# for s in kk:
		
def pra(s):
	for x in s:
		print(x)



def seq_search_ox(s,key):
	if s != []:
		if s[0] == key:
			return True
		else:
			return seq_search_ox(s[1:],key)
	else:
		return False

def seq_search_ox1(s,key):
	while s !=[]:
		if s[0] == key:
			return True
		else:
			s = s[1:]
	return False

def seq_search_ox2(s,key):
	for x in s:
		if x == key:
			return True
	return False

def bin_search_ox(ss,key):
	if ss != []:
		mid = len(ss) // 2
		if key == ss[mid]:
			return True
		elif key < ss[mid]:
			return bin_search_os(ss[:mid],key)
		else:
			return bin_search_os(ss[mid+1:],key)
	else:
		return False

def bin_search(ss,key,low,high):
	if ss != []:
		mid = len(ss) // 2
		if key == ss[mid]:
			return mid
		elif key < ss[mid]:
			return bin_search_ox(ss[:mid])
		else:
			return bin_search(ss[1:])
	else:
		return None

def bin_search_ox1(ss,key):
	while ss != []:
		mid = len(ss) // 2
		if key == ss[mid]:
			return True
		elif key < ss[mid]:
			bin_search_os(ss[:mid],key)
		else:
			bin_search_os(ss[mid+1:],key)
	return False

def seq_search_ox3(ss,key):
	mid = len(ss) // 2
	for x in ss:
		if x == key:
			return True
	return False

def seq_search_ox4(ss,key):
	i = 0
	for x in ss:
		if x == key:
			return i
		i += 1
	return None

import random
def test_seq_search():
	print("Sequential search test")
	db = random.sample(10000,1000)
	for i in range(10):
		key = random.randrange(10000) #키무작위생성
		index = seq_search(db,key)
		print(key,"found at",index)




#-------------------------------------------




test_seq_search()










