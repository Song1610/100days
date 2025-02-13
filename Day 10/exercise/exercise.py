def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True     # print("Leap year") 를 return True로 변경
      else:
        return False    # print("Not leap year")를 return False로 변경
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  year = is_leap(year)

  if month == 2 and year == True:
    month = month_days[month-1] + 1
  else:
    month = month_days[month-1]
  
  return f"{month}"

#🚨 Do NOT change any of the code below 
year = int(input("year : ")) # Enter a year
month = int(input("month : ")) # Enter a month
days = days_in_month(year, month)
print(days)
