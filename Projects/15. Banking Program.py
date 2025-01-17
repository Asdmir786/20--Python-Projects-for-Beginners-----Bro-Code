from os import system
from time import sleep
import json

def frfr(time_in_seconds_for_sleep):
    sleep(time_in_seconds_for_sleep)
    system("cls")
 
def frfrrrr(input_text="Press anything to go to the main screen: "):
    input(input_text)
    system("cls")

def read_data_from_json(balance):
    with open("Projects Resources/balance.json","r") as r:
        data = json.load(r)
    balance = data["balance"]
    return balance
   
def get_balance(balance):
    print(f"Your Balance: Rs. {balance:.2f}")

def deposit_moneh(balance):
    while True:
        try:
            user_deposit_amount = int(input("Enter deposit amount Rs. "))
            if user_deposit_amount <= 0:
                print("Enter a number greater than 0.")
            else:
                break
        except ValueError:
            print("Enter a valid number.")
            frfr(0.3)
        
    temp_balance = user_deposit_amount + balance
    print(f"Deposited Amount: Rs. {user_deposit_amount:.2f}")
    get_balance(temp_balance)
    
    while True:    
        agree = input("Are you sure? (y/n): ").lower().strip()
        if agree == "y" or agree == "":
            return temp_balance
        elif agree == "n":
            return balance
        else:
            print("Incorrect, y or n only.")

def withdraw_money(balance):
    while True:
        try:
            get_balance(balance)
            user_withdraw_amount = int(input("Enter withdrawal amount Rs. "))
            if user_withdraw_amount <= 0:
                print("Enter a number greater than 0.")
                frfr(1)
            elif user_withdraw_amount > balance:
                print(f"Enter a number less than or equal to Rs. {balance:.2f}.")
                frfr(0.5)
            else:
                break
        except ValueError:
            print("Enter a valid number.")
            frfr(1)

    balance -= user_withdraw_amount
    print(f"Withdrawn Amount: Rs. {user_withdraw_amount:.2f}")
    get_balance(balance)
    return balance
    
def save_data_to_json(balance):
    with open("Projects Resources/balance.json", "w") as w:
        json.dump(balance,w,indent=4)
        
    
def main():
    data = {
        "balance":0
    }
    data["balance"] = read_data_from_json(data["balance"])
    while True:
        try:
            print(f"<{'='*10}>")
            print('''What do you want to do:
1. See Balance
2. Deposit Money
3. Withdraw Money
4. Save & Quit''')
            print(f"<{'='*10}>")
            user_input = int(input(": "))
            if user_input not in [1, 2, 3, 4]:
                print("Enter 1, 2, 3, or 4.")
                continue
        except ValueError:
            print("Enter a valid number.")
            frfr(0.7)
            continue
    
        if user_input == 1:
            get_balance(data["balance"])
            frfrrrr()
        elif user_input == 2:
            data["balance"] = deposit_moneh(data["balance"])
            frfrrrr()
        elif user_input == 3:
            data["balance"] = withdraw_money(data["balance"])
            frfrrrr()
        else:
            get_balance(data["balance"])
            save_data_to_json(data)
            input("Data Saved Successfully,\nPress Enter to exit.")
            exit()

if __name__ == "__main__":
    main()
