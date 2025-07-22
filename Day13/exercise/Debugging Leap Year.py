def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:     # 4000 → 400
                return "윤년"       # True
            else:
                return "윤년아님"   # False
        else:
            return "윤년"           # True
    else:
        return "윤년아님"           # False
    


print(is_leap(2021))