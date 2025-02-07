# There are two variables, a and b from input
a = input() # 40
b = input() # 21
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
c = a  #c = 40
a = b  #a = 21
b = c  #b = 40

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


# glass
''' 우리는 glass1과 glass2라는 2개의 변수를 가지고 있습니다.
glass1은 우유를 담고 있고 glass2는 주스를 담고 있습니다.
변수의 내용을 바꾸는 3줄의 코드를 작성하세요. "milk"나 "juice"라는 단어는 입력할 수 없습니다.
이 연습문제를 풀기 위해서만 변수를 사용할 수 있습니다.
'''

glass1 = "milk"
glass2 = "juice"

glass3 = glass1 #glass3 = milk
glass1 = glass2 # glass1 = juice
glass2 = glass3 # glass1 = milk