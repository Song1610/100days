# TODO-1: Ask the user for input
name = input("What is your name?:")  # key
bid = int(input("What is your bid?:"))  # value

bid_dictionary = {}

# TODO-2: Save data into dictionary {name: price}
bid_dictionary[name] = bid

# TODO-3: Whether if new bids need to be added
yes_no = input("Are there any other bidders? Type 'yes' or 'no'.\n")

# TODO-4: Compare bids in dictionary
# max() 이용해서도 작성 가능
# def compare_bid(diction):
#     high_bid = 0
#     winner = ""
#     max(diction)


import art

print(art.logo)


def compare_bid(diction):
    high_bid = 0
    winner = ""
    for name_key in diction:
        bid_value = diction[name_key]
        if bid_value >= high_bid:
            high_bid = bid_value
            winner = name_key
    print(f"The winner is {winner} with a bid of ${high_bid}")


bid_dictionary = {}
bid_question = True

while bid_question:
    name = input("What is your name?:")  # key
    bid = int(input("What is your bid?:"))  # value
    yes_no = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    bid_dictionary[name] = bid

    if yes_no == "yes":
        print("\n" * 20)
    else:
        bid_question = False
        compare_bid(bid_dictionary)



