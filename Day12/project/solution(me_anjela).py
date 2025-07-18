import random       # from random import randint
from art import logo

# todo 4-1 : used global function
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

# todo 3 : function to check user's guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """" Checks answer against guess, returns the number of turns remaining. """
    if user_guess > actual_answer:
        print("too high.")
        return turns - 1
    
    elif user_guess < actual_answer:
        print("too low.")
        return turns - 1
    else :
        print(f"You got it! The answer was {actual_answer}.") 


# todo 4 :  function to set difficulty + used global function 
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else :
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    # todo 1 : choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"Pssst, the correct answer is {answer}")


    turns = set_difficulty()
    


    # todo 5 : repeat the guessing functionality if they get it wrong.
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # todo 2 : let the user guess a number
        guess = int(input("Make a guess: "))

        # track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)         # check_answer() 호출

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")



game()

