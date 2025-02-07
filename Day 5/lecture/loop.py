# loop
# for 형식: 목록의 항목을 살펴보고 각각 항목으로 작업을 수행할 수 있음.
'''
for item in list_of_items:
  print(item)
'''

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

# # range : 반복문을 돌리기 위해 범위의 숫자를 생성하고 싶을 때 사용
# '''
# for number in range(a, b):
#     print(number)
# '''
# for number in range(1, 11, 3):
#     print(number)

# 1부터 100까지의 합 구하기
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# target = 100
# a = 0
# for n in range(1, target + 1):
#     if n % 2 == 0:
#         a += n
# print(a)