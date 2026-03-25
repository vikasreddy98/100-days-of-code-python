import random
import hangman_words
import hangman_art

# Updating the word list
word_list = hangman_words.word_list
lives = 6

# Importing the logo
print(hangman_art.logo)
chosen_word = random.choice(word_list)

# Printing the blank places
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# Main Game Logic
game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"You guessed {guess}. You're one step closer to death!")
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS '{chosen_word}'. YOU'RE HANGED!**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    stages = hangman_art.stages
    print(stages[lives])