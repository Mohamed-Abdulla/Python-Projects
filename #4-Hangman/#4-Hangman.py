import random
from words import words
import string

def valid_words(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper() 

def hangman():
    word=valid_words(words)
    word_letters=set(word)#letters in the word
    alphabet=set(string.ascii_uppercase)
    used_letters=set()#what the user guessed
    lives=6
    #getting user input
    while len(word_letters) >0 and lives>0:
        #letters used
        # ' '.join(['a','b','cd']) -->'a b cd'
        print('You have',lives,' lives left and you have already enter these letters : ',' '.join(used_letters))
        #what current word is (ie W-RD)
        word_list=[letter if letter in used_letters else '-' for letter in word]

        print("Current word : ",' '.join(word_list))
        user_letter=input("Guess a letter :").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1 #takes away a life if wrong
                print('Letter is not in word')
        elif user_letter in used_letters:
            print("You already guessed this letter .. Try another letter")
        else:
            print("Invalid Letter")

    #gets here when len(word_letters) ==0 or when lives ==0
    if lives ==0:
        print('You died,sorry.The word was',word)
    else:
        print('Yay..You guessed the word', word, '!!')
hangman()
        

    