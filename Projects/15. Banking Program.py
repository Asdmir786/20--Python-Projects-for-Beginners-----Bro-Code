from os import system
from time import sleep

def frfr(time_in_seconds_for_sleep):
    sleep(time_in_seconds_for_sleep)
    system("cls")
 
def frfrrrr(input_text="Press Anything to go to Main Screen: "):
    input(input_text)
    system("cls")
   
def get_balance(balance):
    print(f"Your Balance: Rs. {balance:.2f}")

def deposit_moneh(balance):
    while True:
        try:
            user_deposit_amount = int(input("Enter deposit amount Rs. "))
            if user_deposit_amount <= 0:
                print("Enter a number greater than 0.")
            else: break
        except ValueError:
            print("Enter a Number.")
            frfr(0.3)
            
    print(f"Deposited Amount: {user_deposit_amount:.2f}")
    balance = user_deposit_amount + balance
    get_balance(balance)
    return balance

def withdraw_money(balance):
    while True:
        try:
            get_balance(balance)
            user_withdraw_amount = int(input("Gimmeh A Numbah to Al-WithDraw Rs. "))
            if user_withdraw_amount <= 0:
                print("Enter a Numah Greater than 0.")
                frfr(1)
            elif user_withdraw_amount > balance:
                print(f"Enter a Number lowah then {balance:.2f}.")
                frfr(0.5)
            elif user_withdraw_amount < balance: 
                break
        except ValueError:
            print("Enter a Numbah you phool. ")
            frfr(1)

    print(f"Withdraw Amount: {user_withdraw_amount:.2f}")
    balance -= user_withdraw_amount
    get_balance(balance)
    return user_withdraw_amount
    
def main():
    balance = 0
    while True:
        try:
            print(f"<{"="*10}>")
            print('''What do you want to do:
1. See Balance
2. Deposit Moneh
3. Withdraw Moneh
4. Save & Quit''')
            print(f"<{"="*10}>")
            user_input = int(input(": "))
            if user_input not in [1,2,3,4]:
                print("Enter 1 2 3 or 4 plj. ")
                continue
            else: 
                pass
        except ValueError:
            print("Enter a numbah plaese.")
            frfr(0.7)
            continue
    
        if user_input == 1:
            get_balance(balance)
            frfrrrr()
        elif user_input == 2:
            balance += deposit_moneh(balance)
            frfrrrr()
        elif user_input == 3:
            balance -= withdraw_money(balance)
            frfrrrr()
        else:
            get_balance(balance)
            input("frfr bro, press enter or anything to exit: ")
            exit()

if __name__ == "__main__":
    main()