# Write your code here 👇
number = 0
for number in range(1, 101):    
  if (number % 3 != 0) and (number % 5 != 0):
     print(number)
  elif (number % 15 == 0):
     print("FizzBuzz")
  elif (number % 3 == 0):
     print("Fizz")
  elif (number % 5 == 0):
     print("Buzz")