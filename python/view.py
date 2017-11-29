class Reader: 

	@staticmethod 
	def get_number(size):          
		num = input("Type the number you want to move (Type 0 to quit): ")          
		while not (num.isdigit() and 0 <= int(num) <= size * size - 1):              
			num = input("Type the number you want to move (Type 0 to quit): ")          
		return int(num)

class SlidingBoard:

	@staticmethod
	def create_board(board):
		for row in board:
			for num in row:
				if num == 0:
					print("  ",end=" ")
				elif 10 <= num <= 15:
					print(num,end=" ")
				else:
					print(str(num).rjust(2),end=" ")
			print()

	import random
	@staticmethod 
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
	
	@staticmethod 
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

	def print_board(board):
		print("S |  0  1  2  3")
		print("- + -----------")
		i = 0
		for row in self.__board:
			print(i,"|",end=' ')
			for item in row:
				if item == 0:
					print("  ", end=" ")
				elif 10 <= item <= 15:
					print(item,end=" ")
				else:
					print(str(item).rjust(2),end=" ")
			print()
			i += 1

	def move(pos,empty,board):
		(x,y) = pos
		if empty == (x-1,y) or empty == (x+1,y) or \
		   empty == (x,y-1) or empty == (x,y+1):
			board[empty[0]][empty[1]] = board[x][y]
			board[x][y] = 0
			self.__board = board
			self.__empty = pos
			
		else:
			print("Can't move! Try again.")
			self.__board = board
			self.__empty = pos



	def find_position(self, num):      
		for i in range(len(self.__board)):          
			for j in range(len(self.__board)):              
				if num == self.__board[i][j]:                  
					return (i, j)

	def __init__(self, size): 
		self.__board = SlidingBoard.create_init_board(self.__size)
		self.__empty = SlidingBoard.find_position(self)

	@property 
	def board(self): 
		return self.__board


class SlidingBoardcontroller:
	def __init__(self,size):
		self.__slider = SlidingBoard(size)
		self.__goal = SlidingBoard.create_goal_board(size)
		self.__size = size


import sys
if __name__ == "__main__": 
	size = sys.argv[1]      
	if size.isdigit() and int(size) > 1:          
		SlidingPuzzleController(int(size)).play()      
	else:          
		print("Not a proper system argument.")


