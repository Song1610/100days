from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

name = input("What is your name?: ")
price = int(input("What is your bid?: $"))
next = input("Are there any other bidders? Type 'yes or 'no'.\n")

bid = {}

bid(name, price, next)
