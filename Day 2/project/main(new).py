print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100 # 12 -> 0.12
tip_pay = bill * tip_percent    # $100 * 0.12
total_pay = bill + tip_pay  # 100 + 12 = 112
pay = total_pay / people    # 112 / 3
pay_round = round(pay, 2)

print(f"Each person should pay : ${pay_round}")

# other
bill_tip = (tip / 100) * bill + bill
pay2 = round(bill_tip / people, 2)
print(f"Each person should pay : ${pay2}")
