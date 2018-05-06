# def oll(i):
# 	while True:
# 		i = input("i의 값을 입력해주세요: ")
# 		while not (i[1:].isdigit() and (i[0] == "+" or i[0] == "-")) or \
# 			i.isdigit():
# 				print("i의 값이 양수가 아닙니다.")
# 				i = input("i의 다시 값을 입력해주세요: ")
# 		i = int(i)
# 		if i < 0:
# 			print("i의 값이 올바르지 않습니다.")
# 			print("다시 입력해주세요.")
# 			i = input("i의 값을 입력해주세요: ")
# 		else:	
# 			print("good job")
# 		continue1 = input("계속/중지")
# 		countinue1 = ""
# 		while not (continue1 == "계속" or continue1 == "중지"):
# 			continue1 = input("계속/중지 를 입력해주세요")
# 		if continue1 == "중지":
# 			break



def oll(i):
	while True:
		i = input("i의 값을 입력해주세요: ")
		while not ((i[1:].isdigit() and i[0] == "+") or i.isdigit()) :
				print("i의 값이 양수가 아닙니다.")
				i = input("i의 다시 값을 입력해주세요: ")
		i = int(i)
		while i < 0:
			print("i의 값이 올바르지 않습니다.")
			print("다시 입력해주세요.")
			i = input("i의 값을 입력해주세요: ")	
		print("good job")
		continue1 = input("계속/중지")
		countinue1 = ""
		while not (continue1 == "계속" or continue1 == "중지"):
			continue1 = input("계속/중지 를 입력해주세요")
		if continue1 == "중지":
			break

import time
def countdown(s):
	if s > 0:
		print(s)
		time.sleep(1)
		countdown(s-1)
	else:
		print("분석이 완료되었습니다.")

def sigma(s):
	sum = 0
	while s > 0:
		sum = s + sum
		s = s-1
	return sum

import time
def gichan():
	print("""분석은 완료되었으나 당신이 이 시스템을 받아드릴 자격이 있는지
확인이 필요합니다.""")
	time.sleep(1)
	print("이하에 나오는 문제들을 풀어주시기 바랍니다.")
	time.sleep(1)
	print("1부터 50 까지 더해주세요")
	time.sleep(1)
	print("자 한번 풀어보시죠 용사여!")
	r = input("정답은?: ")
	if int(r) != sigma(50):
		print("안타깝군 용사여")
		time.sleep(1)
		print("당신은 자격이 불충분 하시군요! 썩 꺼져주세요!")
		return False
	else:
		print("정답입니다! 당신은 시스템을 열람할 자격이 있습니다!")
	return True




import time
def manghal():
	print("""욕의 세계에 오신 거를 환영합니다.
		다음 3가지 욕 중 1가지를 선택해 주시기 바랍니다.""")
	t = input("씨발, 병신, 개새끼: ")
	while not (t == "씨발" or t == "병신" or t == "개새끼"):
		print("위에 세가지 중에 입력하라고 새끼야.")
		t = input("씨발, 병신, 개새끼: ")
	print("당신은 그런 욕을 좋아 하시는 군요!")
	time.sleep(1)
	print("당신의 성향에 맞는 시스템을 찾아드리겠습니다.")
	countdown(10)
	if t == "씨발":
		if not gichan():
			return None
		print("자 궁금하지 않나요?!?!?!?!?")
		print("두그두그두그두그두그")
		countdown(10)
	elif t == "병신":
		if not gichan():
			return None
		print("자 궁금하지 않나요?!?!?!?!?")
		print("두그두그두그두그두그")
		countdown(10)
	elif t == "개새끼":
		if not gichan():
			return None
		print("자 궁금하지 않나요?!?!?!?!?")
		print("두그두그두그두그두그")
		countdown(10)
	print("자 수고하셨습니다! 헛짓거리를 하셨군요!")
	time.sleep(2)
	while True:
		print("깔깔깔")

def smerge(m,n):
	if m < n:
		return m + smerge(m+1,n)
	else:
		return 0

def smerge1(m,n):
	def loop(m,n,sum):
		if m <= n:
			return loop(m+1,n,m)
		else:
			return loop(m,n,)
	return loop(m,n,sum)
print(smerge1(1,7))















