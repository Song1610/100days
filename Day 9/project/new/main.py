# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)


question = input("Are there any otrher bidders? Type 'yes or no'. \n")
print("\n" * 20)


auction = {}
continue_auction = True

while continue_auction:
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $ "))
    