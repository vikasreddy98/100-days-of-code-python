print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print(r'''
Your mission is to find the treasure.
Lets begin!
''')

player_input = input('You\'re at a crossroad, where do you want to go? '
                     'Left or Right?:\n').lower()
if player_input != "Left":
    print("Fell into a hole. \nGame Over")
elif player_input == "Left":
    player_input=input('You\'ve come to a lake.'
                       'There is an island in the middle of the lake.'
                       'Do you want to:'
                       '"Swim" across? or "Wait" for a boat?\n').lower()
    if player_input != "Wait":
        print("Attacked by trout. \nGame Over")
    elif player_input == "Wait":
        player_input=input('You\'ve arrived at the island unharmed!'
                           'Now, there is a house with 3 doors. Yellow, Red, Blue.'
                           'Which door would you like to open?\n').lower()
        if player_input == "Yellow":
            print("A Wise Choice! You found the Treasure!")
        elif player_input == "Red":
            print("It's a room full of Fire! \nGame Over")
        elif player_input == "Blue":
            print("A room full of  beasts. \nGame Over")
        else:
            print ("That door doesn't exist. Game Over!")