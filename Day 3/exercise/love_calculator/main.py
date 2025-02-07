print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name = name1 + name2

# name count
t1 = name.lower().count('t')
r1 = name.lower().count('r')
u1 = name.lower().count('u')
e1 = name.lower().count('e')
l1 = name.lower().count('l')
o1 = name.lower().count('o')
v1 = name.lower().count('v')

True_name = t1 + r1 + u1 + e1
Love_name = l1 + o1 + v1 + e1


total = int(str(True_name) + str(Love_name))

if (total < 10) or (total > 90):
    print(f"Your score is {total}, you go together like coke and mentos.")
elif (total >= 40) and (total <= 50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")