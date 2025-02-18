# Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# 내가 씀
# for password in range(1, nr_letters + 1):
#     random_letter = random.choice(letters)
#     print(random_letter, end='')

# for password in range(1, nr_symbols + 1):
#     random_symbol = random.choice(symbols)
#     print(random_symbol, end='')

# for password in range(1, nr_numbers + 1):
#     random_number = random.choice(numbers)
#     print(random_number, end='')

# easy
# password = ""
# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char

# for sym in range(1, nr_symbols + 1):
#     random_sym = random.choice(symbols)
#     password += random_sym

# for num in range(1, nr_numbers + 1):
#     random_num = random.choice(numbers)
#     password += random_num

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# 내가 씀
# for pw in range(1, nr_letters + 1):
#     for pw in range(1, nr_symbols + 1):
#         for pw in range(1, nr_numbers + 1):
#             rd_letter = random.choice(letters)
#             rd_symbol = random.choice(symbols)
#             rd_number = random.choice(numbers)
#     print(rd_letter, end='')
#     print(rd_symbol, end='')
#     print(rd_number, end='')

# hard
password_list = []
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password_list.append(random.choice(letters))

for sym in range(1, nr_symbols + 1):
    random_sym = random.choice(symbols)
    password_list += random_sym

for num in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    password_list += random_num

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for result in password_list:
  password += result
print(f"result : {password}")
