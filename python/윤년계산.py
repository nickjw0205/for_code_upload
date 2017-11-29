def isleapyear(year):
	if y % 4 == 0 and (y % 400 == 0 or y % 100 != 0):
		return True
	if y < 0:
		return 0
	else:
		return False


y = int(input())
print(y, isleapyear(y))