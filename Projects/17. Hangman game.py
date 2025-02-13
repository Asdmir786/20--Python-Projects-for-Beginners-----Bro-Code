import sys
sys.path.append("C:\\Users\\asmir\\Documents\\20--Python-Projects-for-Beginners-----Bro-Code")
from ProjectsResources import hangman_game_words as h
import random
import os
import time
import string

lowercase_letters = list(string.ascii_lowercase)

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

def ask_userWord(words_already_done):
    while True:
        print(f"<{"="*40}>\n")
        user_input = input("Guess the word: ").lower().strip()
        if len(user_input) > 1:
            print("Write 1 word at a time.")
        elif user_input in words_already_done:
            print("Enter an alphabet which you have not written.")
        elif user_input not in lowercase_letters:
            print("Enter an Alphabet Bruv.")
        else:
            return user_input

def main():
    main_word = get_word()
    hint = []
    hint.extend(["_"] * len(main_word))
    wrong_guesses = 0
    total_guesses = 0
    alphabets_guessed = {''}
    once = False
    one_hint_available = True
    
    
    while wrong_guesses != len(hangman_states) and "_" in hint:
        frfr = False
        display_state(wrong_guesses)
        for i in hint:
            print(i,end=" ")
        print()
        print(f"Aphabets guessed: {alphabets_guessed}")
        print(f"Wrong Guesses: {wrong_guesses}/{len(hangman_states)}")

        if one_hint_available == True:
            while True:
                user_input = input("Do you want to get a hint or unlock an alphabet (h/a/n): ")
                if user_input == "h":
                    print(f"The hint is: {h.hangman_words_with_hints[f"{main_word}"]}")
                    break
                elif user_input == "a":
                    list_real_words = list(main_word)
                    random_alphabet = random.choice(list_real_words)
                    for k in range(len(main_word)):
                        if random_alphabet == main_word[k]:
                            hint[k] = random_alphabet
                            alphabets_guessed.add(random_alphabet)
                    break
                elif user_input == "n":
                    break
                else:
                    print("Enter one of these: h a or n")
                    clear_screen("ti",1)
        
        if one_hint_available == True:
            alphabets_guessed.remove('')
            display_state(wrong_guesses)    
            for i in hint:
                print(i,end=" ")
            print() 
            one_hint_available = False
            print(f"Aphabets guessed: {alphabets_guessed}")
            print(f"Wrong Guesses: {wrong_guesses}/{len(hangman_states)}")
        word_input = ask_userWord(alphabets_guessed)

        for i in range(len(main_word)):
            if word_input == main_word[i]:
                hint[i] = word_input 
                frfr = True
            
        

        alphabets_guessed.add(word_input) 

        if once == True:
            pass
        else:
            try:
                alphabets_guessed.remove('') 
            except KeyError:
                pass
        once = True
        
        if frfr == True:
            print(f"{word_input} is indeed in the Word.") 

        elif frfr == False:
            print("Nope")
            wrong_guesses += 1
        total_guesses += 1

        clear_screen("ti",1)
        
    if wrong_guesses == len(hangman_states):
        print(f"Too many guesses.\nThe word was: {main_word}")
    else:
        print("Yay you win. fr fr")
    
    
    
if __name__ == "__main__":
    main()