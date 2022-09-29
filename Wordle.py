# File: Wordle.py
​
"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""
​
import random
​
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS,CORRECT_COLOR,PRESENT_COLOR,MISSING_COLOR
​
def wordle():
​
    
    def enter_action(s):
# check to see if input string (s) is within the wordle dictionary (change to lower case for comparison) notify user if it is in the list or noth through the show_message function
        if s.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Congrats, that is in the word list!")
        else:
            gw.show_message("Not in word list")
#parse submitted word into letters for easier functionality
        sLetters = [*s]
        for y, x in enumerate(sLetters):
# check if the letter is in the right position of the word
            if x == keyLetters[y]:
                color = CORRECT_COLOR
# check to see if the letter is in any position for the word
            elif x in keyLetters:
                color = PRESENT_COLOR
# mark letter as not in the word
            else:
                color = MISSING_COLOR
# Change the color of the squre to the assigned letter
            gw.set_square_color(0,y,color) ##############This will have to change once we start working with different rows -----------------------------------------------------------------------------------------------
# initiate wordle window and make enter button active
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
# select a random word from the wordle dictionary
    keyword = FIVE_LETTER_WORDS[random.randint(0,len(FIVE_LETTER_WORDS))].upper()
# split random word into letters for easier management
    keyLetters = [*keyword]
#loop through letters to input on first row of wordle screen
    for y, x in enumerate(keyLetters):
        gw.set_square_letter(0,y,x)
​
# Startup code
​
if __name__ == "__main__":
    wordle()
