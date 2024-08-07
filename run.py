# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# importing words from word_list


import random

# Dictionary of English-Italian translations
translations = {
    "apple": "mela",
    "banana": "banana",
    "orange": "arancia",
    "grape": "uva",
    "strawberry": "fragola",
    "water": "acqua",
    "milk": "latte",
    "bread": "pane",
    "cheese": "formaggio",
    "butter": "burro",
    "car": "macchina",
    "bicycle": "bicicletta",
    "bus": "autobus",
    "train": "treno",
    "airplane": "aeroplano",
    "egg": "uovo",
    "chicken": "pollo",
    "fish": "pesce",
    "shrimp": "gamberetto",
    "juice": "succo",
    "hat": "cappello",
    "belt": "cintura",
    "wood": "legno",
    "moon": "luna",
    "cold": "freddo"
}


def is_valid_input(user_input):
    return user_input.isalpha()


def register_user_name():
    while True:
        name = input("Please enter your name: ").strip()
        if name:
            print(f"Thank you, {name}! you are now registered.")
            return name
        else:
            print("Invalid input.Name cannot be empty.Please try again")


def main_game(name):
    print(f"Hello {name}, let's start playing the game!")


def main_game():
    # Randomly select 10 words from the Dictionary for the game
    words = random.sample(list(translations.keys()), 10)
    score = 0

    print("Welcome/Benvenuti to the English-Italian Translator Game:"
          "\n" "Learn Italian having fun.")
    print("Translate the following words from English to Italian:"
          "\n" "Improve your Italian with us:")

    for word in words:
        user_translation = input(f"Translate '{word}' to Italian: ").strip().lower()
        if user_translation == translations[word]:
            print("Correct!/Giusto")
            score += 1
    else:
        print(f"Incorrect!/Sbagliato The correct translation is'{translations[word]}'.")
        print(f"Game over!/Gioco finito. Your score is {score} out of 10.")


def play_game():
    name = register_user_name()
    while True:
        main_game() #Call the main game function
        while True:
            play_again = input("Do you want to continue/Gioca ancora? (yes/no):").strip().lower()
            if play_again in ('yes', 'no'):
                break
            print("Invalid input.Please type 'yes' or 'no'.")

        if play_again == 'no':
                    print("Thanks/Grazie! Goodbye/Arrivedeci!")
                    break #Breaks the inner loop
                    break


if __name__ == "__main__":
    play_game()
