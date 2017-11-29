def bin_search_ox(ss,key): 
	while ss != []: 
		mid = len(ss) // 2 
		if key == ss[mid]: 
			return True 
		elif key < ss[mid]: 
			ss = ss[:mid] 
		else: 
			ss = ss[mid+1:] 
	return False

def bin_search(ss,key): 
	low = 0 
	high = len(ss) - 1 
	while low <= high: 
		mid = (high + low) // 2 
		if key == ss[mid]: 
			return mid 
		elif key < ss[mid]: 
			high = mid - 1 
		else: 
			low = mid + 1 
	return None

def bin_search_closest(s,key):
	low = 0
	high = len(s)-1
	mid = (low+high)//2
	if s == []:
		return None
	a = []
	while low <= high:
		if key in s:
			index = seq_search(s,key)
			print(key,"found at",index)
		else:
			m = 0
			for x in s:
				if key < s[mid]:
					a.append(abs(key - s[m]))
					m += 1
				else:
					a.append(abs(key - s[m]))
					m += 1
			v = 0
			while a[v] != min(a):
				v += 1
			return v



def testcase():
	db = [3260, 74, 3341, 8122, 6179, 4277, 3266, 5025, 1177, 239, 3561, 1827, 4294,\
	 2766, 2969, 2517, 4189, 3066, 5044, 9623]
	db.sort()
	print("CASE 1")
	print("Expect: The closest value to 70 : 74 at index 0")
	key = 70
	index = bin_search_closest(db,key)
	if(index != None):
		print("Result: The closest value to",key,":",db[index],"at index",index)
		if index == 0:
			print("Correct")
		else:
			print("Failure")
	else:
		print("Result:",key,"found at",index)
		print("Failure")

	print("\nCASE 2")
	print("Expect: The closest value to 3263 : 3260 at index 8")
	print("    OR: The closest value to 3263 : 3266 at index 9")
	key = 3263
	index = bin_search_closest(db,key)
	if(index != None):
		print("Result: The closest value to",key,":",db[index],"at index",index)
		if index == 8 or index == 9:
			print("Correct")
		else:
			print("Failure")
	else:
		print("Result:",key,"found at",index)
		print("Failure")

	print("\nCASE 3")
	print("Expect: The closest value to 9891 : 9623 at index 19")
	key = 9891
	index = bin_search_closest(db,key)
	if(index != None):
		print("Result: The closest value to",key,":",db[index],"at index",index)
		if index == 19:
			print("Correct")
		else:
			print("Failure")
	else:
		print("Result:",key,"found at",index)
		print("Failure")

	print("\nCASE 4")
	print("Expect: 9891 found at None")
	key = 9891
	index = bin_search_closest([],key)
	if(index != None):
		print("Result: The closest value to",key,":",db[index],"at index",index)
		print("Failure")
	else:
		print("Result:",key,"found at",index)
		print("Correct")

testcase()
