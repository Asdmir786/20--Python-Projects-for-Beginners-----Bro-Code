import random

lowest_number = 0
highest_number = 100
target_number  = random.randint(lowest_number,highest_number)
guesses = 0

def tell_numbers(lowest_number,highest_number):
    print(f"The Lowest Number: {lowest_number}.\nThe Highest Number: {highest_number}.")

def ask_user_input(lowest_number,highest_number):
    while True:
        try:
            user_input = int(input("Enter your number: "))
            if user_input < lowest_number or user_input > highest_number:
                print(f"Enter a number less than {highest_number} or greater than {lowest_number}. ")
            else:
                return user_input
        except ValueError:
            print("Enter a number.")
            
def check_guess(user_input,target_number):
    if user_input < target_number:
        print("Too Low, Try Again.") 
        return "Not Won yet"
    elif user_input > target_number:
        print("A Bit High innit.")
        return "Not Won yet"
    elif user_input == target_number:
        print("Yay you win. ")
        return "Win"

def main(lowest_number,highest_number,target_number,guesses):
    tell_numbers(lowest_number,highest_number)
    while True:
        user_input = ask_user_input(lowest_number,highest_number)
        check_win = check_guess(user_input,target_number)
        if check_win == "Not Won yet":
            guesses += 1
            continue
        else:
            print(f"Total Guesses: {guesses}")
            break

if __name__ == "__main__":
    main(lowest_number,highest_number,target_number,guesses)