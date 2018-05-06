def yesno(m):
	yn = input("Yes / No : ")
	while not (yn == "Yes" or yn == "YEs" or yn == "YES" or yn == "YeS" or \
	yn == "yES" or yn == "yes" or yn == "yEs" or yn == "yeS" or yn == "No" or \
	yn == "NO" or yn == "no" or yn == "nO"):
		print("you can only type (Yes / No)")
		yn = input("Yes / No")
def rean(s):
	if yn == "No" or yn == "NO" or yn == "no" or yn == "nO":
		print("please. write what you want to choose one more time.")




def pr(a):
	print("you picked ",a,", Right?")


import time
import random
def real(easy):
	print("""Let's start the game!
The game is simple. you can choose 10 numbers from 1 to 50.
And the computer will choose 10 numbers from 1 to 50,too""")
	time.sleep(3)
	print("""the more numbers you picked are same with what computer picked, 
the more money you will get""")
	print("please type 10 numbers from 1 to 50")
	n = 0
	k = []
	while n != 10:
		l = input("type numbers: ")
	#len을 이용해서 인자의 개수를 확인하자
		while not l.isdigit() or not 0 < int(l) <= 50 or l in k:
			print("you must type the number in 1 to 50 and number must not already typed")
			l = input("type numbers: ")
		k.append(l)
		n += 1
	print("you type this,right?",k,"")
	time.sleep(1)
	s = random.sample(range(50),10)
	print("computer choose",s)
	
import time
import random
def real1(normal):
	print("""Let's start the game!
The game is simple. you can choose 10 numbers from 1 to 100.
And the computer will choose 10 numbers from 1 to 100,too""")
	time.sleep(3)
	print("""the more numbers you picked are same with what computer picked, 
the more money you will get""")
	print("please type 10 numbers from 1 to 100")
	n = 0
	k = []
	while n != 10:
		l = input("type numbers: ")
	#len을 이용해서 인자의 개수를 확인하자
		while not l.isdigit() or not 0 < int(l) <= 100 or l in k:
			print("you must type the number in 1 to 100 and number must not already typed")
			l = input("type numbers: ")
		k.append(l)
		n += 1
	print("you type this,right?",k,"")
	time.sleep(1)
	s = random.sample(range(100),10)
	print("computer choose",s)

import time
import random
def real2(extreme):
	print("""Let's start the game!
The game is simple. you can choose 10 numbers from 1 to 500.
And the computer will choose 10 numbers from 1 to 500,too""")
	time.sleep(3)
	print("""the more numbers you picked are same with what computer picked, 
the more money you will get""")
	print("please type 10 numbers from 1 to 500")
	n = 0
	k = []
	while n != 10:
		l = input("type numbers: ")
	#len을 이용해서 인자의 개수를 확인하자
		while not l.isdigit() or not 0 < int(l) <= 500 or l in k:
			print("you must type the number in 1 to 50 and number must not already typed")
			l = input("type numbers: ")
		k.append(l)
		n += 1
	print("you type this,right?",k,"")
	time.sleep(1)
	s = random.sample(range(500),10)
	print("computer choose",s)
	


def chle(s):
	print("please choose the level you want to play")
	k = input("easy / normal / extreme: ")
	while not(k == "easy" or k == "normal" or k == "extreme"):
		print("please choose in (easy/normal/extreme) and write in small letter")
		k = input("easy / normal / extreme: ")
	if k == "normal":
		print("""you choose 'normal'level.
The game will be started""")
		real1(1)
	if k == "easy":
		print("""you choose 'easy'level.
The game will be started""")
		real(1)
	if k == "extreme":
		print("""you choose 'extreme'level.
The game will be started""")
		real2(2)



import time
def game():
	print("""welclome to the game world
choose the game you want to play""")
	print("A / B / C / D / E")
	print("please type in capital")
	g = input("Which one?: ")
	while not (g == "A" or g == "D" or g == "B" or g == "C" or g == "E"):
		print("please choose in (A,B,C,D,E) and type in capital")
		g = input("Which one?: ")
	if g == "A":
		pr("A")
		yesno("A")
		print(chle(2))
	if g == "B":
		pr("B")
		yesno("B")
		print(chle(2))
	if g == "C":
		pr("C")
		yesno("C")
		print(chle(2))
	if g == "D":
		pr("D")
		yesno("D")
		print(chle(2))
	if g == "E":
		pr("E")
		yesno("E")
		print(chle(2))

			



game()

