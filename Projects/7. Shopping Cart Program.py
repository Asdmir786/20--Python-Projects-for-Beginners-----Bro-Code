import os
import time

items_and_prices = {}
total_price = 0

while True:
    while True:
        user_item = input("Enter a shopping item: ").strip()
        if user_item == "" or user_item == " ":
            print(" Enter a Item plj. ")
            time.sleep(0.5)
            os.system("cls")
        else:
            break

    while True:
        try:
            user_price = float(input(f"Enter the price of {user_item}: "))
            if user_price <= 0:
                print(" Enter a Number above zero plj. ")
                time.sleep(0.5)
                os.system("cls")
            else:
                items_and_prices[user_item] = user_price
                break
        except ValueError:
            print("Choco Aadmi, Number bola jaise 40.68 etc. ")
    
    while True:
            continue_confirmation = input("Do you want to write more or not?(y/n): ").strip()   
            if continue_confirmation == "" or continue_confirmation == " ":
                print("BLOODY y or n.")
            else: break
    
    
                
