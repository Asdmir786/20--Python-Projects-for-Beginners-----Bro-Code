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
    return hint

def ask_userWord():
    while True:
        user_input = input("Guess the word: ").lower().strip()
        if len(user_input) > 1:
            print("Write 1 word at a time.")
        else:
            return user_input

def main():
    main_word = get_word()
    wrong_guesses = 0
    total_guesses = 0
    
    while wrong_guesses != len(hangman_states):
        display_state(wrong_guesses)
        hint = display_hint(main_word)
        word_input = ask_userWord()

        for i in range(len(main_word)):
            if word_input == main_word[i]:
                print(f"{word_input} is indeed in the {main_word}")    
                total_guesses += 1
                break
            else:
                print("Nope")
                total_guesses += 1
                wrong_guesses += 1
                break
    print("Too many guesses")
    
if __name__ == "__main__":
    main()
    