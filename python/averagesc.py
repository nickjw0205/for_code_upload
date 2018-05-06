# 표준입력창에서 점수를 하나씩 차례로 입력받아 평균을 계산하여 내주는 프로시저score_average()를 만들어보자.
# score_average()는 평균을 계산할 때,

# 60점 미만의 과락인 과목은 제외하고 계산해야한다.
# 60점 미만인 과목이 있을 경우 몇 과목인지 알려주어야 한다.
# 계산할 과목이 없으면 평균 점수를 제외하고 출력해야 한다.
# 평균은 소수점 2번째 자리에서 반올림한다.
# score_average() 프로시저를 호출하면 표준입출력창을 통하여 사용자와 대화식으로 프로그램이 아래와 같이 작동한다.

# 다음은 구름 IDE의 실행버튼을 통해서 실행한 결과다.
# 보통 폰트로 된 부분은 컴퓨터가 사용자에게 보여주는 부분(출력)이고,
# 파란색 볼드&이탤릭체로 진하게 보이는 부분이 사용자가 키보드로 입력한 부분(입력)이다.
#------------------------
# 비정상 입력: 3, 정상 입력: 6
# 통과: 6, 과락: 0
# -15
# 120
# 92
# 만점
# 78
# 92
# 88
# 64
# 95
# 0
# 6
# 84.8
#-----------------------
def score_average1():
	count = 0
	total = 0
	average = 0
	while True:
		score = input("")
		if score.isdigit() and 60 <= int(score) <=100:
			total = total + int(score)
			count = count + 1
		if int(score) == 0:
			break
	averge = round(total/count,2)
	print(count)
	print(round(total/count))
	if 0 <= count < 6:
		print(6 - count)

def score_average():
	count = 0
	total = 0
	failed = 0
	while True:
		score = input("")
		if int(score) == 0:
			return False
		while not score.isdigit() or not 0<=int(score)<=100:
			score = input("")
			if int(score) <= 60:
				failed += 1
			if 60 <= int(score) <= 100:
				total += int(score)
				count += 1
	print(count)
	if count != 0:
		print(round((total/count),1))
	if failed != 0:
		print(failed)
score_average1() 














