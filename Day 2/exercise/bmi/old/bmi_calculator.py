# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

h = float(height)
w = float(weight)

bmi = w / (h ** 2)
b = int(bmi)

print(b)