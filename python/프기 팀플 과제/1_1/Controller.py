from tkinter import *
from model import *
from view import *
# 이 파일을 터미널에서 실행하시면 됩니다.
# 맨 처음에 제일 상단에 Level(라디오 버튼)을 누르시고 start버튼을 누르시면 게임이 시작됩니다.
# 구멍의 수는 Hard = 40, Normal = 34, Easy = 28개입니다.
 
# 그 후 입력하고자하는 좌표값을 x,y에 넣고 num에 답을 적으시면됩니다.
# input 버튼을 누르면 답을 제출하는 것이고
# Memo는 점수에 상관없이 num을 메모하고자 하는 것입니다.
# 어떤 num을 넣어야 할지 모르겠으면 ? 버튼을 누르시면 됩니다.

# Save는 현재 스코어와 보드를 각각 score.txt, board.txt에저장하는 기능이고
# Load는 score.txt, board.txt에서 이전에 저장하는 값을 불러오는 버튼입니다.

# System문구는 버튼을 누른 후 메세지를 나타내줍니다.
# 게임이 시작되면 "Game Start!!!"
# 입력값이 틀렸을 경우 "Wrong position (x, y), input num"
# 값을 입력하지 않고 버튼을 누르면 "Please Input Value"
# 스도쿠를 완성하였을 경우 "Congratulation! 'score', you awarded 'rank'!"가 표시됩니다.
class SudokController:
	def __init__(self):
		'''initialize SudokController'''
		self.window = Tk()
		self.window.title("Sudoku")
		self.window.geometry("500x550")
		self.window.resizable(False, False)

		events = {"start":self.start_event,"input":self.input_event,"memo":self.memo_event,"save":self.save_event,"load":self.load_event, "idk":self.idk_event}
		self.screen = ScreenManager(self.window, events)
		self.start = False

		self.window.mainloop()

	def start_event(self,level):
		'''start button event'''
		if(level == 0):
			return
		self.start = True
		self.sboard = SudokBoard(level, [])
		self.screen.print_board(self.sboard.board)

	def input_event(self, x, y, num):
		'''input button event'''
		self.initEntry()
		if(not(self.start)):
			return

		if 0 in (len(x),len(y),len(num)):
			self.screen.print_message("Please Input Value")
			return

		x, y, num = int(x) - 1, int(y) - 1, int(num)
		blank = self.sboard.get_blank((x, y));

		if blank['state'] == SudokBoard.state_solve:
			return

		if blank['num'] == num:
			blank['state'] = SudokBoard.state_solve
			blank['penalty'] += 3
		else:
			self.screen.print_message("Wrong position ("+str(x+1)+", "+str(y+1)+"), input "+str(num))
			blank['penalty'] -= 1

		self.sboard.change_blank((x, y), blank)
		self.screen.print_board(self.sboard.board)

		if self.sboard.holes == 0:
			ll = Data.Load_score()
			sco = Data.Get_score(self.sboard.board)
			rank = 1
			for i in range(len(ll)):
				if ll[i] < sco:
					rank += 1
				else:
					break
			Data.Save_score(sco)
			self.screen.print_message("Congratulation! "+str(sco)+", you awarded "+str(rank)+"!")

	def idk_event(self,x, y):
		'''? button event'''
		self.initEntry()
		if(not(self.start)):
			return

		if 0 in (len(x),len(y)):
			self.screen.print_message("Please Input Value")
			return

		x, y = int(x) - 1, int(y) - 1
		blank = self.sboard.get_blank((x, y));

		if blank['state'] in (SudokBoard.state_unsolve, SudokBoard.state_idk, SudokBoard.state_memo) :
			blank['state'] = SudokBoard.state_idk
			self.screen.print_board(self.sboard.board)

	def memo_event(self,x, y, num):
		'''memo button event'''
		self.initEntry()
		if(not(self.start)):
			return

		if 0 in (len(x),len(y),len(num)):
			self.screen.print_message("Please Input Value")
			return

		x, y, num = int(x) - 1, int(y) - 1, int(num)
		blank = self.sboard.get_blank((x, y));

		if blank['state'] in (SudokBoard.state_unsolve, SudokBoard.state_idk, SudokBoard.state_memo) :
			blank['state'] = SudokBoard.state_memo
			blank['memo'] = num
			self.sboard.change_blank((x, y), blank)
			self.screen.print_board(self.sboard.board)
	
	def save_event(self):
		'''save button event'''
		if(not(self.start)):
			return
		Data().Save_board(self.sboard.board)

	def load_event(self):
		'''load button event'''
		self.start = True
		self.sboard = Data.Load_board()

		self.screen.print_board(self.sboard.board)

	def initEntry(self):
		'''initialize Entries'''
		self.screen.xEntry.delete(0,END)
		self.screen.yEntry.delete(0,END)
		self.screen.numEntry.delete(0,END)
		
if __name__ == '__main__':
	'''start Game'''
	SudokController()