def get_number():
	num = input("Type the number you want to move(Type 0 to quit): ")
	while not(num.isdigit()) and 0 <= int(num) <= size*size:
		num = input("Type the number you want to move(Type 0 to quit): ")
	return int(num)


def move(pos,empty,board):
	(x,y) = pos
	if empty == (x-1,y) or empty == (x+1,y) or \
	empty == (x,y-1) or empty == (x,y+1):
		board[empty[0]][empty[1]] = board[x][y]
		board[x][y] = 0
		return (pos,board)
	else:
		print("Can't move! Try again.")
		return (empty,board)


import random
def create_init_board(size):
	k = []
	s = []
	for i in range(0,size*size):
		s.append(i)
	k = random.sample(s,size**2)
	l = []
	m = []
	for x in range(1,size*size+1):
		if x % int(size) != 0:
			l.append(k[x-1])
		else:
			l.append(k[x-1])
			m.append(l)
			l = []
	return m

def print_board(board):
	for row in board:
		for num in row:
			if num == 0:
				print("  ",end=" ")
			elif 10 <= num <= 15:
				print(num,end=" ")
			else:
				print(str(num).rjust(2),end=" ")
		print()

def create_goal_board(size):
	k = []
	for i in range(1,size**2):
		k.append(i)
	k.append(0)
	z = []
	s = []
	n = 0
	if size >2:
		while n != size**2:
			if n != 1 and n != 0:
				if (n+1) % size != 0:
					s.append(k[n])
				else:
					s.append(k[n])
					z.append(s)
					s = []	
				n = n + 1
			elif n == 1:
				s.append(k[n])
				n = n+1
			else:
				s.append(k[n])
				n = n+1
		return z
	else:
		while n != size**2:
			if n == 0:
				s.append(k[n])
				n += 1
			elif n ==1:
				s.append(k[n])
				z.append(s)
				n += 1
				s = []
			elif n == 2:
				s.append(k[n])
				n = n+1
			else:
				s.append(k[n])
				z.append(s)
				s = []
				n += 1
		return z
def get_number():
	num = input("Type the number you want to move(Type 0 to quit): ")
	while not num.isdigit() or  not (0 <= int(num) <= (int(size)**2 -1)):
		num = input("Type the number you want to move(Type 0 to quit): ")
	return int(num)


def move(pos,empty,board):
	(x,y) = pos
	if empty == (x-1,y) or empty == (x+1,y) or \
	empty == (x,y-1) or empty == (x,y+1):
		board[empty[0]][empty[1]] = board[x][y]
		board[x][y] = 0
		return (pos,board)
	else:
		print("Can't move! Try again.")
		return (empty,board)

def find_position(num,board):
	for i in range(int(size)):
		for j in range(int(size)):
			if num == board[i][j]:
				return (i,j)
				

def sliding_puzzle(size):
	board = create_init_board(size)
	goal = create_goal_board(size)
	empty = find_position(0,board) 
	while True: 
		print_board(board)
		if board == goal:  
			print("Congratulations!") 
			break 
		num = get_number() 
		if num == 0:  
			break 
		pos = find_position(num, board) 
		(empty, board) = move(pos, empty, board)    
	print("Please come again.")




if __name__ == "__main__": 
	import sys 
	size = sys.argv[1] 
	if size.isdigit() and int(size) > 1: 
		sliding_puzzle(int(size)) 
	else: 
		print("Not a proper system argument.")