import random
class SudokBoard:

	level_hard = 40
	level_normal = 34
	level_easy = 28

	state_solve = 0
	state_unsolve = 1
	state_memo = 2
	state_idk = 3

	def __init__(self, holes, board):
		'''initialize SudokBoard'''
		if board != []:
			self.__holes = holes
			self.__board = board
		else:
			self.__holes = holes
			a = self.__listboard()
			self.__board = []
			for i in range(9):
				self.__board.append([])
			for i in range(9):
				for j in range(9):
					self.__board[i].append({'state':SudokBoard.state_solve,'text':"",'num':a[i][j],'penalty':0,'memo':0})
			self.mk_holes(holes)


	def __listboard(self):
		'''return : board in CLI version'''
		seed = [1,2,3,4,5,6,7,8,9]
		random.shuffle(seed)
		n1 = seed[0]
		n2 = seed[1]
		n3 = seed[2]
		n4 = seed[3]
		n5 = seed[4]
		n6 = seed[5]
		n7 = seed[6]
		n8 = seed[7]
		n9 = seed[8]			
		return [[n1,n2,n3,n4,n5,n6,n7,n8,n9],
				[n4,n5,n6,n7,n8,n9,n1,n2,n3],
				[n7,n8,n9,n1,n2,n3,n4,n5,n6],
				[n2,n3,n1,n5,n6,n4,n8,n9,n7],
				[n5,n6,n4,n8,n9,n7,n2,n3,n1],
				[n8,n9,n7,n2,n3,n1,n5,n6,n4],
				[n3,n1,n2,n6,n4,n5,n9,n7,n8],
				[n6,n4,n5,n9,n7,n8,n3,n1,n2],
				[n9,n7,n8,n3,n1,n2,n6,n4,n5]]

	@property
	def board(self):
		'''return : board'''
		return self.__board

	@property
	def holes(self):
		'''return : holes'''
		return self.__holes

	def mk_holes(self,holes):
		'''make holes in board'''
		while holes > 0:
			i = random.randint(0,8)
			j = random.randint(0,8)
			if self.__board[i][j]['state'] != SudokBoard.state_unsolve:
				self.__board[i][j]['state'] = SudokBoard.state_unsolve
				holes -= 1

	def get_blank(self,pos):
		'''get blank which in pos\nreturn : {"state", "memo", "num", "text", "penalty"} dictionary'''
		return self.__board[pos[1]][pos[0]]

	def change_blank(self, pos, blank):
		'''change blank which in pos'''
		self.__board[pos[1]][pos[0]] = blank
		if blank['state'] == SudokBoard.state_solve:
			self.__holes -= 1

class Data:

	@staticmethod
	def Get_score(board):
		'''Get Score From Board\nreturn:total score'''
		ptotal = 0
		for i in range(9):
			for j in range(9):
				ptotal += board[i][j]['penalty']
		return 100 + 10 * ptotal


	@staticmethod
	def Save_score(score):
		'''Save Score To File'''
		t = open("score.txt",'a')
		t.write(str(score)+"\n")
		t.close()

	@staticmethod
	def Load_score():
		'''Load Score From File\nreturn : score list'''
		t = open("score.txt","r")
		
		score = []
		for line in t:
			score.append(int(line))

		sorted(score, reverse = True)
		print(score)

		t.close()
		return score

	@staticmethod
	def Save_board(board):
		'''Save Board To File'''
		t = open("board.txt","w")
		for i in range(9):
			for j in range(9):
				t.write(str(board[i][j]['state'])+","+board[i][j]['text']+","+str(board[i][j]['num'])+","+str(board[i][j]['penalty'])+","+str(board[i][j]['memo'])+"\n")
		t.close()

	@staticmethod
	def Load_board():
		'''Load Board From File\nreturn : SudokBoard object'''
		board = [[],[],[],[],[],[],[],[],[]]
		i = 0
		try:
			t = open("board.txt","r")
		except FileNotFoundError:
			return SudokBoard(SudokBoard.level_normal)
		
		holes = 0

		for line in t: 
			state, text, num, penalty, memo = line.strip('\n').split(',')
			if int(state) != SudokBoard.state_solve:
				holes += 1
			board[i//9].append({'state':int(state),'text':text,'num':int(num),'penalty':int(penalty),'memo':memo})
			i+=1
		t.close()
		return SudokBoard(holes, board)