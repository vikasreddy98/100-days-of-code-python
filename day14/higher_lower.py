from art import logo, vs
from game_data import data
import random

def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return(f"{account_name}, a {account_description}, from {account_country}")

def check_answer(u_guess, a_followers, b_followers):
    if a_followers > b_followers:
        if u_guess == 'a':
            return True
        else:
            return False
    else:
        if u_guess == 'b':
            return True
        else:
            return False

print(logo)

score = 0
game_on = True
account_b = random.choice(data)


while game_on:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)} ")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    correct = check_answer(guess, a_followers, b_followers)

    if correct:
        score += 1
        print(f"Correct! Current Score: {score}")
        print("\n" * 20)

    else:
        print(f"Wrong! Final Score: {score} ")
        game_on = False

