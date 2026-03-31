import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(my_list):
    if my_list != [11,10] or my_list != [10,11]:
        return sum(my_list)
    if sum(my_list) > 21:
        if 11 in my_list:
            my_list.remove(11)
            my_list.append(1)
        return my_list
    else:
        return 0

def compare(uname, cname):
    if uname == cname:
        return "Draw 🙃"
    elif cname == 0:
        return "Lose, opponent has Blackjack 😱"
    elif uname == 0:
        return "Win with a Blackjack 😎"
    elif uname > 21:
        return "You went over. You lose 😭"
    elif cname > 21:
        return "Opponent went over. You win 😁"
    elif uname > cname:
        return "You win 😃"
    else:
        return "You lose 😤"

def blackjack():
    print(logo)
    user = []
    computer = []
    game_over = False
    user_score = -1
    comp_score = -1
    for i in range(2):
        user.append(deal_card())
        computer.append(deal_card())
    while not game_over:
        user_score = calculate_score(user)
        comp_score = calculate_score(computer)
        print(f"\tYour cards: {user}, current score: {sum(user)}")
        print(f"\tComputer's first card: {computer[0]}")
        if comp_score == 0 or  user_score == 0 or user_score > 21:
            game_over = True
        else:
            draw_card = input("Type 'y' to get another card or type 'n' to pass: ")
            if draw_card == "y":
                user.append(deal_card())
            else:
                game_over = True
    while comp_score != 0 and comp_score < 17:
        computer.append(deal_card())
        comp_score = calculate_score(computer)
    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    blackjack()