# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#importing words from word_list


import random 

from words import words_list

#function of the game play and rules!

def play_game(word_list):
    print("Welcome to the English-Italian translation game!")
    print("Translate the English word to Italian.Type'exit' to quit.\n") 

    #Shuffle the words

    english_words = list(words.keys())
    random.shuffle(english_words)

    score = 0 

    for english_word in english_words:
        italian_translation = words[english_word]