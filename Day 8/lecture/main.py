# funtion의 기본 유형
'''
def my_function():
  여기에 적절한걸 넣으면 됨
'''

# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# Greeting()이라는 함수를 만듭니다.
# 함수 안에 3개의 print 문을 작성합니다.
# Greeting() 함수를 호출하고 코드를 실행합니다.

def greet():
  print("no.1"),
  print("no.2"),
  print("no.3"),
  print("")
greet()


# function wuth inputs
'''
def my_function(something):    # 괄호 안에 변수의 이름 추가
  이것
  저것
  그것
'''

def greet_with_name(name):
  print(f"hi, {name}!")
  print(f"how do you do {name}!")
  print("")

greet_with_name("mingyu")

############################
# function that allow for input
'''
parameter : 전달되는 데이터의 이름
argument : 데이터의 실제 값
'''

# function with more than 1 input
def greet_with(name, location):
  print(f"hello {name}!")
  print(f"what is it like in {location}")
  print("")
greet_with("jun","china")
#         ---------------- <- positional Argument

# keyword arguments
''' def my_function(a=1, b=2, c=3):
  this b
  that c
  else a
print -> this 2, that 3, else 1
'''

greet_with(location= "cadana", name="mingyu")


