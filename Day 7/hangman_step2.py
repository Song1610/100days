#Step 2

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-1: - 디스플레이라는 빈 목록을 만듭니다.
# selected_word의 각 문자에 대해 'display'에 "_"를 추가합니다.
#따라서 selected_word가 "apple"인 경우, 추측할 각 문자를 나타내는 5개의 "_"가 포함된 ["_", "_", "_", "_", "_"]가 표시되어야 합니다.
display = []
word_len = len(chosen_word)
for n in range(word_len):
    display = display + ["_"]

print(display)

guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-2: - selected_word의 각 위치를 반복합니다.
#해당 위치의 문자가 '추측'과 일치하면 해당 위치의 디스플레이에 해당 문자를 표시합니다.
#예: 사용자가 "p"를 추측했고 선택한 단어가 "apple"인 경우에는 ["_", "p", "p", "_", "_"]가 표시되어야 합니다.
for position in range(word_len):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
#TODO-3: - 'display'를 인쇄하면 추측한 문자가 올바른 위치에 있고 다른 모든 문자는 "_"로 대체되는 것을 볼 수 있습니다.
#힌트 - 사용자가 다음 글자를 추측하게 만드는 것에 대해 걱정하지 마세요. 이 문제는 3단계에서 다루겠습니다.

print(display)
