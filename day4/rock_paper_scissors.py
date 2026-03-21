import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock Paper Scissors game!")

choice = [rock, paper, scissors]
index = random.randint(0, len(choice)-1)

player_choice= int(input("What do you choose? \n0 for ROCK \n1 for PAPER \n2 for SCISSOR \n"))
computer_choice = index

print(choice[player_choice])
print("Computer chose:")
print(choice[computer_choice])

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == 0 and computer_choice ==1:
    print("You lose!")
elif player_choice == 1 and computer_choice == 0:
    print("You win!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 2 and computer_choice == 0:
    print("You lose!")
elif player_choice == 1 and computer_choice == 2:
    print("You lose!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("Invalid Choice! Game Over!")
