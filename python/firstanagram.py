def anagram():
	memo = [0]*(10000)
	k = ['0952', '5239', '1270', '8581', '7458', '3414', '7906', '2356','4360',\
	'3491', '6232', '5927', '2735', '2509', '5849', '8457', '9340', '1858', '8602', '5784']
	s = 0
	a = []
	q = []
	w = []
	for i in range(10):
		for j in range(10):
			for z in range(10):
				for x in range(10):
					memo[s] = str(i)+str(j)+str(z)+str(x)
					if memo[s] in k and not memo[s] in q:
						q.append(memo[s])
						a.append(memo[s])
						if str(i)+str(j)+str(x)+str(z) in k and str(i)+str(j)+str(z)+str(x) != str(i)+str(j)+str(x)+str(z):						
							a.append(str(i)+str(j)+str(x)+str(z))
							q.append(str(i)+str(j)+str(x)+str(z))
						if str(i)+str(z)+str(j)+str(x) in k and str(i)+str(j)+str(z)+str(x) != str(i)+str(z)+str(j)+str(x):
							a.append(str(i)+str(z)+str(j)+str(x))
							q.append(str(i)+str(z)+str(j)+str(x))
						if str(i)+str(z)+str(j)+str(x) in k and str(i)+str(j)+str(z)+str(x) != str(i)+str(z)+str(j)+str(x):
							a.append(str(i)+str(z)+str(j)+str(x))
							q.append(str(i)+str(z)+str(j)+str(x))
						if  str(i)+str(z)+str(x)+str(j) in k and str(i)+str(j)+str(z)+str(x) != str(i)+str(z)+str(x)+str(j):
							a.append(str(i)+str(z)+str(x)+str(j))
							q.append(str(i)+str(z)+str(x)+str(j))
						if str(i)+str(x)+str(z)+str(j) in k and str(i)+str(j)+str(z)+str(x) != str(i)+str(x)+str(z)+str(j):
							a.append(str(i)+str(x)+str(z)+str(j))
							q.append(str(i)+str(x)+str(z)+str(j))
						if str(i)+str(x)+str(j)+str(z) in k and str(i)+str(j)+str(z)+str(x) != str(i)+str(x)+str(j)+str(z):
							a.append(str(i)+str(x)+str(j)+str(z))
							q.append(str(i)+str(x)+str(j)+str(z))
						if str(j)+str(i)+str(z)+str(x) in k and str(i)+str(j)+str(z)+str(x) != str(j)+str(i)+str(z)+str(x):
							a.append(str(j)+str(i)+str(z)+str(x))
							q.append(str(j)+str(i)+str(z)+str(x))
						if str(j)+str(i)+str(x)+str(z) in k and str(i)+str(j)+str(z)+str(x) != str(j)+str(i)+str(x)+str(z):
							a.append(str(j)+str(i)+str(x)+str(z))
							q.append(str(j)+str(i)+str(x)+str(z))
						if str(j)+str(x)+str(i)+str(z) in k and str(i)+str(j)+str(z)+str(x) != str(j)+str(x)+str(i)+str(z):
							a.append(str(j)+str(x)+str(i)+str(z))
							q.append(str(j)+str(x)+str(i)+str(z))
						if str(j)+str(x)+str(z)+str(i) in k and str(i)+str(j)+str(z)+str(x) != str(j)+str(x)+str(z)+str(i):
							a,append(str(j)+str(x)+str(z)+str(i))
							q.append(str(j)+str(x)+str(z)+str(i))
						if str(j)+str(z)+str(x)+str(i) in k and str(i)+str(j)+str(z)+str(x) != str(j)+str(z)+str(x)+str(i):
							a.append(str(j)+str(z)+str(x)+str(i))
							q.append(str(j)+str(z)+str(x)+str(i))
						if str(j)+str(z)+str(i)+str(x) in k and str(i)+str(j)+str(z)+str(x) != str(j)+str(z)+str(i)+str(x):
							a.append(str(j)+str(z)+str(i)+str(x))
							q.append(str(j)+str(z)+str(i)+str(x))
						if str(z)+str(i)+str(x)+str(j) in k and str(i)+str(j)+str(z)+str(x) != str(z)+str(i)+str(x)+str(j):
							a.append(str(z)+str(i)+str(x)+str(j))
							q.append(str(z)+str(i)+str(x)+str(j))
						if str(z)+str(i)+str(j)+str(x) in k and str(i)+str(j)+str(z)+str(x) != str(z)+str(i)+str(j)+str(x):
							a.append(str(z)+str(i)+str(j)+str(x))
							q.append(str(z)+str(i)+str(j)+str(x))
						if str(z)+str(x)+str(i)+str(j) in k and str(i)+str(j)+str(z)+str(x) != str(z)+str(x)+str(i)+str(j):
							a.append(str(z)+str(x)+str(i)+str(j))
							q.append(str(z)+str(x)+str(i)+str(j))
						if str(z)+str(x)+str(j)+str(i) in k and str(i)+str(j)+str(z)+str(x) != str(z)+str(x)+str(j)+str(i):
							a.append(str(z)+str(x)+str(j)+str(i))
							q.append(str(z)+str(x)+str(j)+str(i))
						if str(z)+str(j)+str(i)+str(x) in k and str(i)+str(j)+str(z)+str(x) != str(z)+str(j)+str(i)+str(x):
							a.append(str(z)+str(j)+str(i)+str(x))
							q.append(str(z)+str(j)+str(i)+str(x))
						if str(z)+str(j)+str(x)+str(i) in k and str(i)+str(j)+str(z)+str(x) != str(z)+str(j)+str(x)+str(i):
							a.append(str(z)+str(j)+str(x)+str(i))
							q.append(str(z)+str(j)+str(x)+str(i))
						if str(x)+str(i)+str(z)+str(j) in k and str(i)+str(j)+str(z)+str(x) != str(x)+str(i)+str(z)+str(j):
							a.append(str(x)+str(i)+str(z)+str(j))
							q.append(str(x)+str(i)+str(z)+str(j))
						if str(x)+str(z)+str(i)+str(j) in k and str(i)+str(j)+str(z)+str(x) != str(x)+str(z)+str(i)+str(j):
							a.append(str(x)+str(z)+str(i)+str(j))
							q.append(str(x)+str(z)+str(i)+str(j))
						if str(x)+str(i)+str(j)+str(z) in k and str(i)+str(j)+str(z)+str(x) != str(x)+str(i)+str(j)+str(z):
							a.append(str(x)+str(i)+str(j)+str(z))
							q.append(str(x)+str(i)+str(j)+str(z))
						if str(x)+str(z)+str(j)+str(i) in k and str(i)+str(j)+str(z)+str(x) != str(x)+str(z)+str(j)+str(i) != str(j)+str(z)+str(x)+str(i):
							a.append(str(x)+str(z)+str(j)+str(i))
							q.append(str(x)+str(z)+str(j)+str(i))
						if str(x)+str(j)+str(i)+str(z) in k and str(i)+str(j)+str(z)+str(x) != str(x)+str(j)+str(i)+str(z):
							a.append(str(x)+str(j)+str(i)+str(z))
							q.append(str(x)+str(j)+str(i)+str(z))
						if str(x)+str(j)+str(z)+str(i) in k and str(i)+str(j)+str(z)+str(x) != str(x)+str(j)+str(z)+str(i):
							a.append(str(x)+str(j)+str(z)+str(i))
							q.append(str(x)+str(j)+str(z)+str(i))
						if not str(i)+str(z)+str(j)+str(x) in k and not str(i)+str(j)+str(x)+str(z) in k and not \
str(i)+str(z)+str(x)+str(j) in k and not \
str(i)+str(x)+str(z)+str(j) in k and not str(i)+str(x)+str(j)+str(z) in k and not str(j)+str(i)+str(z)+str(x) in k and not \
str(j)+str(i)+str(x)+str(z) in k and not str(j)+str(x)+str(i)+str(z) in k and not str(j)+str(x)+str(z)+str(i) in k and not \
str(j)+str(z)+str(x)+str(i) in k and not str(j)+str(z)+str(i)+str(x) in k and not str(z)+str(i)+str(x)+str(j) in k and not \
str(z)+str(i)+str(j)+str(x) in k and not str(z)+str(x)+str(i)+str(j) in k and not str(z)+str(x)+str(j)+str(i) in k and not \
str(z)+str(j)+str(i)+str(x) in k and not str(z)+str(j)+str(x)+str(i) in k and not str(x)+str(i)+str(z)+str(j) in k and not \
str(x)+str(i)+str(j)+str(z) in k and not str(x)+str(z)+str(i)+str(j) in k and not str(x)+str(z)+str(j)+str(i) in k and not \
str(x)+str(j)+str(i)+str(z) in k and not str(x)+str(j)+str(z)+str(i) in k:
							a = []
						if a != []:
							if len(a) != 1:
								for l in range(len(a)):
									print(a[l],end =" ")
								print()
						a = []
					s += 1


anagram()

