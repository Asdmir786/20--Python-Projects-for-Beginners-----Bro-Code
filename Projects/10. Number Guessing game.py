import random

lowest_number = 0
highest_number = 100

target_number  = random.randint(lowest_number,highest_number)

def tell_numbers():
    print(f"The Lowest Number: {lowest_number}.\nThe Highest Number: {highest_number}.")

def ask_user_input():
    while True:
        try:
            user_input = int(input("Enter your number: "))
            if lowest_number <= user_input >= highest_number:
                return user_input
            else:
                print(f"Enter a number less than {highest_number} or graeter than {lowest_number}. ")
        except ValueError:
            print("Enter a number.")
            
