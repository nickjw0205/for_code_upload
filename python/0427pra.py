# 다이나믹 프로그래밍 ---> 동적계획법
# 2차원 리스트 --> 열안에 열로 만들고 table[][]f로  부름 (table)은 이름 마은대로 지어도 상괸없음
# 행= 세로 열=가로

def fib(n):  
	if n > 1: 
		return fib(n - 1) + fib(n - 2) 
	else: 
		return n

def fib(n): 
	i = 1 
	bunny, rabby = 1, 0 
	while i < n: 
		i += 1 
		bunny, rabby = rabby, bunny + rabby 
	return bunny + rabby

def fib(n):
	bunny, rabbit = 1, 0
	while n >0:
		bunny, rabbit = rabbit, bunny + rabbit
		n -= 1
	return bunny + rabbit


# def fib(n): 
# 	i = 1      
# 	bunny, rabby = 1, 0      
# 	while i < n:          
# 		i += 1
# 		temp = bunny          
# 		bunny = rabby          
# 		rabby = temp + rabby      
# 		return bunny + rabby


# def fib(n): 
# 	bunny, rabby = 1, 0     
# 	for i in range(2, n + 1):          
# 		bunny, rabby = rabby, bunny + rabby      
# 		return bunny + rabby


# def fib(n): 
# 	bunny, rabby = 1, 0      
# 	for _ in range(2, n + 1):          
# 		bunny, rabby = rabby, bunny + rabby      
# 		return bunny + rabby




def fibseq(n): 
	fibs = [0, 1] 
	for k in range(2, n + 1): 
		fibs.append(fibs[k - 1] + fibs[k - 2]) 
	return fibs

def comb(n, r): 
	if not (r == 0 or r == n): 
		return comb(n - 1, r - 1) + comb(n - 1, r) 
	else: 
		return 1

def comb_pascal(n, r): 
	matrix = [[]] * (n - r + 1) 
	matrix[0] = [1] * (r + 1) 
	for i in range(1, n - r + 1): 
		matrix[i] = [1] 
	for i in range(1, n - r + 1): 
		for j in range(1, r + 1): 
			newvalue = matrix[i][j - 1] + matrix[i - 1][j] 
			matrix[i].append(newvalue) 
	return matrix[n - r][r]

def hanoitower(n, source, destination, temp) : 
	if n > 1 : 
		hanoitower(n - 1, source, temp, destination) 
		print("move from", source, "to", destination) 
		hanoitower(n - 1, temp, destination, source) 
	else : 
		print("move from", source, "to", destination)

hanoitower(100,1,3,2)

