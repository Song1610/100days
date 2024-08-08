#Step 5
from replit import clear
import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
import hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
import hangman_art

logo = hangman_art.logo

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    #TODO-4: - 사용자가 이미 추측한 문자를 입력한 경우 문자를 인쇄하여 알려주세요.
    if guess in display:
        print(f"You've already guessed {guess}.")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(
        #     f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
        # )
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        #TODO-5: - 문자가 chosen_word에 없으면 문자를 인쇄하여 해당 단어에 없다고 알려주세요.
        print(f"You guessed {guess}, that's not in the word. you lose a life.")
      
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    stages = hangman_art.stages
    print(stages[lives])
