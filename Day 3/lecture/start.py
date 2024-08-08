# # 욕조 예시
water_level = int(input("water_level: "))
if water_level > 80 :
  print("Drain water")
else:
  print("continue")



print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    elif age <= 23:
        print("Please pay $10.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# # 부등호
# >
# <
# >=
# <=
# ==
# !=
