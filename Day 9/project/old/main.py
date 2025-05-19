from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bid = {}
# 입찰이 끝났는지 계속 추적할 수 있는 변수가 있어야함
bidding_finished = False

def find_highest_bidder(data):
  # data = {"ming" : "$170"}
  highest_bid = 0
  for people in data:
    amount = data[people]
    if amount > highest_bid:
      highest_bid = amount
      winner = people
  print(f"winner = {winner}, bid = ${highest_bid}")
      
  
while not bidding_finished : 
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bid[name] = price
  next = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if next == "no":
    bidding_finished = True
    find_highest_bidder(bid)
  elif next == "yes":
    clear()

