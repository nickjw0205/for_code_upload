def anagram():
	memo = []
	memo1 = []
	k = ['0952', '5239', '1270', '8581', '7458', '3414', '7906', '2356', '4360', \
	'3491', '6232', '5927', '2735', '2509', '5849', '8457', '9340', '1858', '8602', '5784']
	for i in range(len(k)):
		for j in range(4):
			memo1.append(k[i][j])
		memo1.sort()
		memo.append(memo1)
		memo1 = []
	idk = []
	hgs = []
	for x in range(len(k)):
		for z in range(len(memo)):
			if not x == z:
				if memo[z] == memo[x]:
					if not k[z] in hgs:
						idk.append(k[z])
						hgs.append(k[z])
					if not k[x] in hgs:
						idk.append(k[x])
						hgs.append(k[x])
		if idk != []:
			for h in range(len(idk)):
				print(idk[h],end =" ")
			print()
		idk = []
anagram()



