alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
#TODO-1: encrypt() 및 decrypt() 함수를 caesar()라는 단일 함수로 결합합니다.

# def caesar(plain_text, shift_amount, cipher_direction):
#     this_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         if cipher_direction == "decode":
#             new_position = position - shift_amount
#             this_text += alphabet[new_position]
#         elif cipher_direction == "encode":
#             new_position = position + shift_amount
#             this_text += alphabet[new_position]
#     print(f"The {cipher_direction}d text is {this_text}")

# caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)

# 안젤라ver
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")




#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
#TODO-2: 'text', 'shift' 및 'direction' 값을 전달하여 Caesar() 함수를 호출합니다.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
