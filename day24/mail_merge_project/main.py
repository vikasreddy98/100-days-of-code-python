PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letters = letter_file.read()

    for name in names:
        stripped = name.strip()
        new_letter = letters.replace(PLACEHOLDER, stripped)
        with open(f"./Output/ReadyToSend/letter_for_{stripped}.txt", "w") as complete_letter:
            complete_letter.write(new_letter)
