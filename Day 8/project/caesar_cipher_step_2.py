alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""  # 빈 변수 정의
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#TODO-1: 'text'와 'shift'를 입력으로 사용하는 'decrypt'라는 다른 함수를 만듭니다.


#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#TODO-2: 'decrypt' 함수 내에서 'text'의 각 문자를 알파벳에서 *뒤로* 이동한 양만큼 이동하고 해독된 텍스트를 인쇄합니다.
#e.g.
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"
def decrypt(cipher_text, shift_a):
    plain_text = ""  # 빈 변수 정의
    for i in cipher_text:
        de_position = alphabet.index(i)
        plain_position = de_position - shift_a
        decrypt_text = alphabet[plain_position]
        plain_text += decrypt_text
        # decrypt_text += alphabet[plain_position] 와 같다.
    print(f"The decoded text is {plain_text}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
#TODO-3: 'direction' 변수를 확인하여 사용자가 메시지를 암호화하거나 해독하기를 원했는지 확인하세요. 그런 다음 해당 '방향' 변수를 기반으로 올바른 함수를 호출하십시오. 메시지를 암호화하고 *복호화하는 코드를 테스트할 수 있어야 합니다.

if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_a=shift)