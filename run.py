# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#importing words from word_list



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

def play_game():
    # Randomly select 10 words from the dictionary for the game
    words = random.sample(list(translations.keys()), 10)
    score = 0

    print("Welcome/Benvenuti to the English-Italian Translator Game!")
    print("Translate the following words from English to Italian:")

    for word in words:
        user_translation = input(f"Translate '{word}' to Italian: ").strip().lower()
        if user_translation == translations[word]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct translation is '{translations[word]}'.")

    print(f"Game over!/Gioco finito Your score is {score} out of 10.")

if __name__ == "__main__":
    play_game()