import random
from words import words
import string



def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # getting user input
while len(word_letters) > 0:
     
    
    
    user_letter = input("Guess the letter").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in wrod_letters:
            word_letters.remove(user_letter)
            
    elif user_letter in used_letters:
        print("You have already used that character. please try again.")

    else:
        print("Invalid charecter. Please try again.")

user_input = input("Type somthing")
print(user_input)