import os
import random as r
import time

options = ["rock", "paper", "scissors"]

def ask_user_input():
    while True:
            user_choice = input(f"Enter Your Choice({', '.join(options)}): ").lower().strip()
            if user_choice not in options:
                print("Try Again. ")
                time.sleep(.5)
                os.system("cls")
            else:
                return user_choice

def get_random_choice():
    computer_choice = r.choice(options)
    return computer_choice

def cheen_tapak_dam_dam(user_choice,computer_choice):
    def user_wins():
        print(f"You choose: {user_choice}\nComputer choose: {computer_choice}\n User Wins.")
        return "user_wins"
    def computer_wins():
        print(f"You choose: {user_choice}\nComputer choose: {computer_choice}\n User Wins.")
        return "computer_wins"
    def draw():
        print(f"You choose: {user_choice}\nComputer choose: {computer_choice}\n User Wins.")
        return "draw"

    if user_choice == computer_choice:
        draw()
    # computer wins
    elif user_choice == "rock" and computer_choice == "paper" or user_choice == "paper" and computer_choice == "scissor" or user_choice == "scissor" and computer_choice == "rock":
        computer_wins()
    # user wins
    else:
        user_wins()

ask_user_input()