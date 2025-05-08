alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.

# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.



##### 1st 작성 #####
def caesar(encode_or_decode, original_text, shift_amount):
    cipher_abc = ""
    for a in original_text:
        if encode_or_decode == "encode":
            cipher_position = alphabet.index(a) + shift_amount
        else:
            cipher_position = alphabet.index(a) - shift_amount
        cipher_position %= len(alphabet)
        cipher_abc += alphabet[cipher_position]
    print(f"{encode_or_decode} result : {cipher_abc}")


##### 2rd 수정 #####
def caesar(encode_or_decode, original_text, shift_amount):
    cipher_abc = ""
    for a in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1

        cipher_position = alphabet.index(a) + shift_amount
        cipher_position %= len(alphabet)
        cipher_abc += alphabet[cipher_position]
    print(f"{encode_or_decode} result : {cipher_abc}")

caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)