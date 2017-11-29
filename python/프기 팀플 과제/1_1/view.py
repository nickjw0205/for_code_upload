from tkinter import *
from model import *

class ScreenManager(Frame):
	def __init__(self, root, events):
		"""initialize ScreenManager"""
		super().__init__(root)
		self.pack()
		self.__getLevelFrame(events['start']).pack()
		self.__getBoardFrame().pack()
		self.__getInputFrame(events).pack()
		self.__getSystemFrame().pack()

	def __getLevelFrame(self, start_event):
		'''return : level selection frame'''
		lFrame = Frame(self)		
		self.__level = IntVar()

		Radiobutton(lFrame, text="Hard",
			value=SudokBoard.level_hard, variable = self.__level
			).grid(row=0, column=0)

		Radiobutton(lFrame, text="Normal",
			value=SudokBoard.level_normal, variable = self.__level
			).grid(row=0, column=1)

		Radiobutton(lFrame, text="Easy",
			value=SudokBoard.level_easy, variable = self.__level
			).grid(row=0, column=2)

		Button(lFrame, text="start", 
			command=lambda : start_event(self.__level.get())
			).grid(row=1, column=1)

		return lFrame

	def __getBoardFrame(self):
		'''return : board frame'''
		bFrame = Frame(self)

		for i in range(1,10):
			l = Label(bFrame , text=i)
			l.grid(row = 0, column = i)

		for i in range(1,10):
			l = Label(bFrame , text=i)
			l.grid(row = i, column = 0)

		self.__boardLabel = []
		self.__gridInfo = {}
		for y in range(9):
			row = []
			for x in range(9):
				if (x//3 + y//3) % 2 == 0:
					l = Label(bFrame , text="", width=4, height=2,borderwidth = 1, relief="groove",bg=Color.panelColors[1])
					self.__gridInfo[str(l)] = (x+1,y+1)
					l.bind("<Button-1>",self.mouseClick)
				else:
					l = Label(bFrame , text="", width=4, height=2,borderwidth = 1, relief="groove",bg=Color.panelColors[0])
					self.__gridInfo[str(l)] = (x+1,y+1)
					l.bind("<Button-1>",self.mouseClick)
				l.grid(row = y+1, column = x+1)
				row+=[l]

			self.__boardLabel += [row]
		return bFrame
	def mouseClick(self,event):
		self.xEntry.delete(0,END)
		self.yEntry.delete(0,END)
		self.xEntry.insert(0,self.__gridInfo[str(event.widget)][0])
		self.yEntry.insert(0,self.__gridInfo[str(event.widget)][1])

	def __getInputFrame(self, events):
		'''return : input frame'''
		iFrame = Frame(self)	

		Label(iFrame, text="x").grid(row=0, column=0)
		Label(iFrame, text="y").grid(row=0, column=1)
		Label(iFrame, text="num").grid(row=0, column=2)

		self.xEntry = Entry(iFrame, width = 5,justify = 'center')
		self.xEntry.bind('<KeyPress>', self.keyPress)
		self.xEntry.grid(row=1, column=0)

		self.yEntry = Entry(iFrame, width = 5,justify = 'center')
		self.yEntry.bind('<KeyPress>', self.keyPress)
		self.yEntry.grid(row=1, column=1)

		self.numEntry = Entry(iFrame, width = 5,justify = 'center')
		self.numEntry.bind('<KeyPress>', self.keyPress)
		self.numEntry.grid(row=1, column=2)

		Button(iFrame, text="Input", 
			command=lambda : events["input"](self.xEntry.get(), self.yEntry.get(), self.numEntry.get())
			).grid(row=2, column=0)

		Button(iFrame, text="Memo", 
			command=lambda : events["memo"](self.xEntry.get(), self.yEntry.get(), self.numEntry.get())
			).grid(row=2, column=1)

		Button(iFrame, text="?", 
			command=lambda : events["idk"](self.xEntry.get(), self.yEntry.get())
			).grid(row=2, column=2)
		
		Button(iFrame, text="Save", 
			command=events["save"]
			).grid(row=3, column=0)

		Button(iFrame, text="Load", 
			command=events["load"]
			).grid(row=3, column=1)

		return iFrame

	def __getSystemFrame(self):
		'''return : system label frame'''
		sFrame = Frame(self)
		self.sys = Label(sFrame, text="System : Please Select level and start!")
		self.sys.pack()

		return sFrame

	def keyPress(self,event):
		'''event for key press\nreturn : fuction name'''
		keyCount = len(event.widget.get())

		if event.keysym in ('Right','Left','BackSpace', 'Tab'):
			if(keyCount > 0 and event.keysym == 'BackSpace'):
				keyCount -= 1
				
		elif not(keyCount == 0 and event.char.isdigit()):
			return 'break'

		else:
			if(int(event.char) == 0):
				return 'break'
			keyCount += 1

	def print_message(self, msg):
		'''print message to System Label'''
		self.sys['text'] = "System : "+msg;

	def print_board(self, board):
		'''print board to Labels'''
		for y in range(9):
			for x in range(9):
				state, num, penalty, memo = board[y][x]['state'], board[y][x]['num'], board[y][x]['penalty'], board[y][x]['memo']
				if state == SudokBoard.state_solve:
					self.__boardLabel[y][x].configure(fg = "black")
					self.__boardLabel[y][x]['text'] = str(num)

				elif state == SudokBoard.state_unsolve:
					self.__boardLabel[y][x].configure(fg = "black")
					self.__boardLabel[y][x]['text'] = ''
				
				elif state == SudokBoard.state_memo:
					self.__boardLabel[y][x].configure(fg = "gray")
					self.__boardLabel[y][x]['text'] = memo

				elif state == SudokBoard.state_idk:
					self.__boardLabel[y][x].configure(fg = "gray")
					self.__boardLabel[y][x]['text'] = "?"

				if penalty < 0:
					a = abs(penalty)
					if a > 0:
						self.__boardLabel[y][x].configure(bg = Color.penaltyColors[a-1])
					else:
						self.__boardLabel[y][x].configure(bg = "#ED0000")
				elif penalty > 0:
					self.__boardLabel[y][x].configure(bg = Color.plusColors[3 - abs(penalty)])
				else:
					if (x//3 + y//3) % 2 == 0:
						self.__boardLabel[y][x].configure(bg = Color.panelColors[1])
					else:
						self.__boardLabel[y][x].configure(bg = Color.panelColors[0])



class Color:
	'''Color Definitions'''
	penaltyColors = ["#FFC6C6", "#FFA2A2", "#FF7E7E", "#FF5A5A", "#FF3636", "#FF1212", "#ED0000"]
	plusColors = ["#53FF4C", "#ADFFA6", "#D1FFCA"]
	panelColors = ["white", "#CACFD2"]