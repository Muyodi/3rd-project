# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#importing words from word_list


import random 
from words import words_list


words = {
"Apple": "Mela",
"Banana": "Banana", 
"Egg": "Uovo",  
"Chicken": "Pollo",   
"Fish": "Pesce",  
"Shrimp": "Gamberetto", 
"Juice": "Succo",  
"Water": "Acqua",  
"Skirt": "Gonna",
"Hat": "Cappello", 
"Belt": "Cintura",  
"Wood": "Legno", 
"Moon": "Luna", 
"Cold": "Freddo",
"Month": "Mese"

}


#function of the game play and rules!

def play_game():
    print("Welcome to the English-Italian translation game!")
    print("Translate the English word to Italian.Type'exit' to quit.\n") 

    #Shuffle the words

    english_words = list(words.keys())
    random.shuffle(english_words)

    score = 0 

    for english_word in english_words:
        italian_translation = words[english_word]

        user_translation = input(f"What is the Italian word for'{english_word}'? ").strip().upper()
        if user_translation == "exit":
            break

        if user_translation == italian_translation:
            print("Correct!\n")
            score += 1

        else:
            print(f"Wrong. The correct translation is '{italian_translation}'.\n")
            print(f"Game Over! Your final score is {score}out of {len(english_words)}.")

            #Start the game
play_game()
