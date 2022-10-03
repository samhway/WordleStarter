# File: Wordle.p

# Sam Holloway, Sierra Griffin, Adam Blackham, Madison Coffey, Glenn Livingston (Group 14)
# Project 5
# Last Updated: October 3, 2022
# Create a project like wordle in python
#

from asyncio import events
import random
from this import s

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS,CORRECT_COLOR,PRESENT_COLOR,MISSING_COLOR

def wordle():

    
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
# check if user entered correct word
        if  keyword == s:
# Congratulatory message
            gw.show_message("Congrats, you guessed the WORDLE")
        else:
# move onto next line if word not guess correctly ( set_current_row and get_current_row) 
            gw.get_current_row()
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





# Startup code

if __name__ == "__main__":
    wordle()
