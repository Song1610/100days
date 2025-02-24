#Step 3

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
#TODO-1: - 사용자가 다시 추측할 수 있도록 하려면 while 루프를 사용하세요. 루프는 사용자가 selected_word의 모든 문자를 추측하고 'display'에 더 이상 공백("_")이 없는 경우에만 중지되어야 합니다. 그런 다음 사용자에게 승리했음을 알릴 수 있습니다.

end_game = False  # 변수 생성
while not end_game:
    guess = input("Guess a letter: ").lower()
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(
        #         f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
        #     )
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_game = True
        print("끝")
