import os
import time

items_and_prices = {}
total_price = 0

def get_userItem():
    while True:
        user_item = input("Enter a shopping item: ").strip()
        if user_item == "" or user_item == " ":
            print(" Enter a Item plj. ")
            time.sleep(0.5)
            os.system("cls")
        else:
            return user_item

def get_userItemPrice(user_item):
    while True:
        try:
            user_price = float(input(f"Enter the price of {user_item}: "))
            if user_price <= 0:
                print(" Enter a Number above zero plj. ")
                time.sleep(0.5)
                os.system("cls")
            else:
                return user_price
        except ValueError:
            print("Choco Aadmi, Number bola jaise 40.68 etc. ")

def get_userConfirmation(user_item, user_price):
    while True:
        user_confirmation = input(f"Are you sure you want to add {user_item} for Rs.{user_price:.2f}? (y/n): ").strip()
        if user_confirmation == "" or user_confirmation == " ":
            print("BLOODY y or n.")
        else:
            return user_confirmation

def add_item_to_cart(user_item, user_price):
    global items_and_prices
    items_and_prices[user_item] = user_price
    print(f"{user_item} has been added to the cart for Rs.{user_price:.2f}.")

def display_cart():
    print("\n<==========Shopping Cart==========>\n")
    for count, (item, price) in enumerate(items_and_prices.items(), start=1):
        print(f"{count}. {item}: Rs.{price:.2f}")
    print(f"\nTotal Price: Rs.{sum(items_and_prices.values()):.2f}")
    
def get_userChoiceForMore():
    while True:
        user_choice = input("Do you want to add more items to the cart? (y/n): ").strip()
        if user_choice.lower() != "y":
            display_cart()
            input("\nPress Enter to exit...")
            os.system("cls")
            return False
        else:
            display_cart()
            input("\nPress Enter to exit...")
            os.system("cls")
            return True
    
def main():
    while True:
        user_item = get_userItem()
        user_price = get_userItemPrice(user_item)
        user_confirmation = get_userConfirmation(user_item, user_price)
        if user_confirmation.lower() == "y":
            add_item_to_cart(user_item, user_price)
        else:
            print(f"{user_item} has not been added to the cart.")
            
        if not get_userChoiceForMore():
            break
        else:
            continue
        
if __name__ == "__main__":
    main()