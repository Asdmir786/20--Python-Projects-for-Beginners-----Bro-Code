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

def ask_userWord():
    while True:
        print(f"<{"="*40}>\n")
        user_input = input("Guess the word: ").lower().strip()
        if len(user_input) > 1:
            print("Write 1 word at a time.")
        else:
            return user_input

def main():
    main_word = get_word()
    hint = []
    hint.extend(["_"] * len(main_word))
    wrong_guesses = 0
    total_guesses = 0
    
    
    while wrong_guesses != len(hangman_states) and "_" in hint:
        frfr = False
        display_state(wrong_guesses)
        for i in hint:
            print(i,end=" ")
        print()
        word_input = ask_userWord()

        for i in range(len(main_word)):
            if word_input == main_word[i]:
                print(f"{word_input} is indeed in the {main_word}") 
                hint[i] = word_input 
                frfr = True
                
        if frfr == False:
            print("Nope")
            wrong_guesses += 1
        total_guesses += 1

        clear_screen("ti",1)
        
    if wrong_guesses == len(hangman_states):
        print("Too many guesses")
    else:
        print("Yay you win. fr fr")
    
    
    
if __name__ == "__main__":
    main()
    