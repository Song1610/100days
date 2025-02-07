height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)

print(bmi)

# 추가 : 정수(int)로 나타내기
print(int(bmi))         # 30

# 추가 : 반올림(round)로 나타내기
print(round(bmi))       # 31
print(round(bmi, 2))    # 30.85