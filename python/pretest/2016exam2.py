### 반 : 화 / 금
### 이름 :
### 학번 :

#### 2 ####
# 문자열 내에 특정 문자가 나타나는 횟수를 내주는 함수

def occurred_in(char, string):
	occ = 0
	for c in string:
		if c == char:
			occ += 1
	return occ

# print(occurred_in('p', '')) # 0
# print(occurred_in('p', 'I love Python!')) # 0
# print(occurred_in('e', 'What happened to your college life?')) # 5

#### 3 ####

def numbers_art(n):
	for i in range(n):
		for j in range(n):
			print(j+1, end=' ')
		print()

# numbers_art(5)
# numbers_art(7)

# (1)
def numbers_art1(n):
	while n >0:
		for i in range(n):
			print(i+1,end = " ")
		print()
		n -= 1

# (2)
def numbers_art2(n):
	a = 1
	while a < n+1:
		for i in range(a):
			print(i+1,end =" ")
		print()
		a += 1


# (3)
def numbers_art3(n):
	for i in range(n):
		for j in range(n):
			if j+1 > i:
				print(j+1,end = " ")
			else:
				print(" ",end = " ")
		print()




# (4)
def numbers_art4(n):
	a = n
	for i in range(n):
		for j in range(n):
			if j+1 >= a:
				print(j+1,end = " ")
			else:
				print(" ",end = " ")
		a -= 1
		print()

# numbers_art1(5)
# numbers_art2(5)
# numbers_art3(5)
# numbers_art4(5)


##### 4 #####

# 인수 n이 소수인지 확인하기
def is_prime(n):
	if n < 2:
		return False
	else:
		for i in range(2,n):
			if n % i == 0:
				return False
		return True

# for i in range(50):
# 	if is_prime(i):
# 		print(i)

# (1)
def is_prime(n):
	if n < 2:
		return False
	else:
		for i in range(2,n):
			if n % 2 == 0:
				return False
			else:
				if n % i == 0:
					return False
		return True

# for i in range(50):
# 	if is_prime(i):
# 		print(i)

# (2)
# 자연수 n미만의 소수를 2부터 시작하여 모두 오름차순으로 나열한 리스트로 만들어 내주는 함수
def primes_less_than(n):
	p = []
	a = 0
	j = 2
	x = 0
	if n < 2:
		pass
	else:
		if n > 2:
			p.append(2)
			for i in range(2,n):
				while i > j:
					if i % 2 == 0:
						x += 1
					elif i % j == 0:
						x += 1
					else:
						a += 1
					j += 1
				if a != 0 and x == 0:
					p.append(i)
				a = 0
				j = 2
				x = 0
	return p



# print(primes_less_than(2)) # []
# print(primes_less_than(3)) # [2]
# print(primes_less_than(10)) # [2, 3, 5, 7]
# print(primes_less_than(30)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# (3)
# k개의 소수를 2부터 시작하여 오름차순으로 리스트로 만들어 내주는 함수
def primes(k):
	p = []
	n = 2
	while k > 0:
		if is_prime(n) == True:
			p.append(n)
		if len(p) == k:
			break
		n += 1
	return p

# print(primes(0)) # []
# print(primes(1)) # [2]
# print(primes(5)) # [2, 3, 5, 7, 11]
# print(primes(10)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# (4)
# 쌍둥이 소수 k 쌍 찾기 (차이가 2인 소수의 쌍)
def twin_primes(k):
	p = []
	a = []
	prev = 2
	n = 3
	while k > 0:
		if is_prime(n) == True:
			a.append(n)
		if len(a) == 3:
			if int(a[1]) - int(a[0]) == prev:
				p.append((a[0],a[1]))
				k -= 1
			a.remove(a[0])
		n += 1
	return p

# print(twin_primes(0)) # []
# print(twin_primes(1)) # [(3, 5)]
# print(twin_primes(5)) # [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31)]
# print(twin_primes(10)) 
#[(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73), (101, 103), (107, 109)]


#### 5 ####

# (1)
## generate all subsequences

def subsequences(ns):
	subs = [[]]
	for n in ns:
		newsubs = []
		for sub in subs:
			newsubs.append([sub + [n]])

		subs += newsubs
	return subs

# print(subsequences([])) 
# [[]]
# print(subsequences([1]))
# [[], [1]]
# print(subsequences([1,2]))
# [[], [1], 
#  [2], [1, 2]]
# print(subsequences([1,2,3]))
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# print(subsequences([1,2,3,4]))
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], 
#  [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]

# (2)
# check if a list is increasing
def increasing(ns):
	a = len(ns)
	if a > 1:
		for i in range(1,a):
			if ns[i-1] >= ns[i]:
				return False
		return True
	else:
		return True


# print(increasing([])) # True
# print(increasing([2])) # True
# print(increasing([1,2])) # True
# print(increasing([2,2])) # False
# print(increasing([3,2])) # False
# print(increasing([1,2,3])) # True
# print(increasing([1,3,2])) # False
# print(increasing([3,2,1])) # False

# (3)
# length of longest increasing subsequence
def longest_increasing_subsequence(ns):
	if len(ns) < 2:
		return len(ns)
	else:
		subs = subsequences(ns)
		longest = 1
		for sub in subs:
			pass # fill me in
		return longest

# print(longest_increasing_subsequence([])) # 0
# print(longest_increasing_subsequence([3])) # 1
# print(longest_increasing_subsequence([5,4])) # 1
# print(longest_increasing_subsequence([2,4])) # 2
# print(longest_increasing_subsequence([4,3,2])) # 1
# print(longest_increasing_subsequence([4,2,7,5,9])) # 3
# print(longest_increasing_subsequence([4,2,7,5,4,7,6,8,9,6])) # 5

#### 6 ####

# (1)
# 2진수를 10진수로 바꾸기

def bin2dec(bin):
	length = len(bin)
	dec = 0
	for i in range(length):
		dec += int(bin[i]) * 2**(length-i-1)
	return dec

# print(bin2dec('0')) # 0
# print(bin2dec('1')) # 1
# print(bin2dec('110')) # 6
# print(bin2dec('10011')) # 19
# print(bin2dec('101010')) # 42

# (2)
# 10진수를 2진수로 바꾸기

def dec2bin(dec):
	bin = ''
	while not (dec == 0 or dec == 1):
		bin = str(dec % 2) + bin
		dec = dec//2
	bin = str(dec) + bin
	return bin

# print(dec2bin(0)) #=> '0'
# print(dec2bin(1)) #=> '1'
# print(dec2bin(6)) #=> '110'
# print(dec2bin(19)) #=> '10011'
# print(dec2bin(42)) #=> '101010'



