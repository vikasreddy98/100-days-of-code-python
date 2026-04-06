from art import logo
import random

hard_diff = 5
easy_diff = 10

def difficulty():
    diff = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if diff == 'easy':
        return easy_diff
    else:
        return hard_diff

def check_answer(user_guess, comp_guess, turns):
    if user_guess < comp_guess:
        print("Go Higher!")
        turns -= 1
        return turns
    elif user_guess > comp_guess:
        print("Go Lower!")
        turns -= 1
        return turns
    else:
        print(f"{comp_guess} it is! Well done!")

def guess_the_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = difficulty()

    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts left to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You're out of attempts. Please refresh the page to play again.")
            return

guess_the_number()