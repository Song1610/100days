import random
from hangman_words import name_list
from hangman_art import stages, logo

chosen_word = random.choice(name_list)
end_game = False
lives = 6

print(logo)
# print(chosen_word)
print(f"lives: {lives}")

# word display
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)


while not end_game:
  # guess input
  guess = input("입력하세요: ").lower()

  if guess in display:
    print(f"aready {guess}")
  
  # check guessd speling
  for position in range(word_length):
      spel = chosen_word[position]
      if spel == guess:
          display[position] = spel
          
  # lives 감소
  if guess not in chosen_word:
    print(f"your guessed {guess}, you lose a life. X_X")
    lives -= 1
    print(f"lives is {lives}")
  
  print(f"{' '.join(display)}")
  
  # display
  if "_" not in display:
    end_game = True
    print("you win")
  elif lives == 0:
    end_game = True
    print("you lose!")

  print(stages[lives])