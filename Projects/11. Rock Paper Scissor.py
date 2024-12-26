import os
import random as r
import time

options = ["rock", "paper", "scissors"]

def ask_user_input():
    while True:
            os.system("cls")
            user_choice = input(f"Enter Your Choice({', '.join(options)}): ").lower().strip()
            if user_choice not in options:
                print("Try Again. ")
                time.sleep(.5)
                os.system("cls")
            else:
                return user_choice

def get_random_choice():
    return r.choice(options)

def cheen_tapak_dam_dam(user_choice,computer_choice):
    def user_wins():
        print(f"\nYou choose: {user_choice}\nComputer choose: {computer_choice}\nUser Wins.")
    def computer_wins():
        print(f"\nYou choose: {user_choice}\nComputer choose: {computer_choice}\nComputer Wins.")
    def draw():
        print(f"\nYou choose: {user_choice}\nComputer choose: {computer_choice}\nDraw.")

    if user_choice == computer_choice:
        draw()
        return "draw"
    # computer wins
    elif (user_choice == "rock" and computer_choice == "paper")\
         or (user_choice == "paper" and computer_choice == "scissors")\
         or (user_choice == "scissors" and computer_choice == "rock"):
        computer_wins()
        return "computer_wins"
    # user wins
    else:
        user_wins()
        return "user_wins"

def continue_or_not():
    while True:
        user_choice = input("Do you want to Continue?(y/n)\n:").lower().strip()
        if user_choice not in ["y","n"]:
            print("Enter y or n.")
            os.system("cls")
        elif user_choice == "y":
            break
        elif user_choice == "n":
            print("Bye bye.")
            input("Press Enter to exit the program...")
            exit()
            

def main():

    while True:
        user_choice = ask_user_input()
        computer_choice = get_random_choice()
        calculator = cheen_tapak_dam_dam(user_choice,computer_choice)
        
        if  calculator == "draw":
            time.sleep(0.5)
            input("Press Enter to continue... ")
            os.system("cls")
            continue
        elif calculator == "user_wins":
            print("Yay You WIN FR FR.")
            continue_or_not()
        elif calculator == "computer_wins":
            print("Yay You LOSE FR FR.")
            continue_or_not()
            
if __name__ == "__main__":        
    main()