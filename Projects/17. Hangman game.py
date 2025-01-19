import sys
sys.path.append("C:\\Users\\asmir\\Documents\\20--Python-Projects-for-Beginners-----Bro-Code")
from ProjectsResources import hangman_game_words as h
import random
import os
import time

hangman_states = [
    """
       _______
      |/      |
      |       
      |       
      |        
      |       
     _|___    
    """,
    """
       _______
      |/      |
      |      ( )
      |       
      |        
      |       
     _|___    
    """,
    """
       _______
      |/      |
      |      ( )
      |       |
      |        
      |       
     _|___    
    """,
    """
       _______
      |/      |
      |      ( )
      |      /|
      |        
      |       
     _|___    
    """,
    """
       _______
      |/      |
      |      ( )
      |      /|\\
      |        
      |       
     _|___    
    """,
    """
       _______
      |/      |
      |      ( )
      |      /|\\
      |      / 
      |       
     _|___    
    """,
    """
       _______
      |/      |
      |      ( )
      |      /|\\
      |      / \\
      |       
     _|___    
    """
]

def get_word():
    word = random.choice(h.words)
    return word

def display_state(number=0):
    print(hangman_states[number])

def clear_screen(userInput_or_timeInput="",seconds=0,prompt="Press enter or anything to clear screen.\n: "):
    userInput_or_timeInput =  userInput_or_timeInput.lower().strip()
    
    if userInput_or_timeInput == "ui":
        input(prompt)
        os.system("cls")
    else:
        time.sleep(seconds)
        os.system("cls")
    
def display_hint(word):
    hint = "_ "*len(word)
    print(hint)

