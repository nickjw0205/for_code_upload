def days_in_month(year,month): # 아래 True를 적절한 논리식으로 바꾸자.
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        if month == 2:# True를 적절한 논리식으로 바꾸자.
            return 29
        if month ==1 or 2 < month <13:
            if month % 2 != 0: # True를 적절한 논리식으로 바꾸자.
                return 31
        elif 7 < month <= 12:
            if month %2 != 0:
                return 30
            else:
                return 31

    else: # True를 적절한 논리식으로 바꾸자.
        if 0 < month <= 7:
            if month % 2 != 0: # True를 적절한 논리식으로 바꾸자.
                return 31
            else:
                return 30
        elif 7 < month <= 12:
            if month %2 != 0:
                return 30
            else:
                return 31
        else:
            return 0


print(days_in_month(2016,4)) # => 30
print(days_in_month(2016,12)) # => 31
print(days_in_month(2016,2)) # => 29
print(days_in_month(2017,2)) # => 28
print(days_in_month(2016,13)) # => 0

















