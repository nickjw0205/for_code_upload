def ssort0(s):
	if s != []: 
		smallest = min(s)
		s.remove(smallest)
		return [smallest] + ssort0(s)
	else:
		return[]


s = [1,2,3,4,4,5,6,345,6,4]
print(ssort0(s))