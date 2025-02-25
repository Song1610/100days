#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# word_list에서 무작위로 단어를 선택하고 변수에 할당합니다.
import random

chosen_word = random.choice(word_list)
# print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# 사용자에게 문자를 추측하고 추측이라는 변수에 답을 할당하도록 요청합니다. 추측을 소문자로 만드세요.
guess = input("입력: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# 사용자가 추측한 문자가 chosen_word의 문자 중 하나인 지 확인합니다.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
