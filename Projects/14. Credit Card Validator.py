import time
import os
    
def frfr(time_in_seconds_for_sleep):
    time.sleep(time_in_seconds_for_sleep)
    os.system("cls")
    
def get_credit_card_number():
    while True:
        cc_number = input("Enter your credit card number (you can use spaces, dashes, or just enter it continuously): ").strip()
        if cc_number == "" or cc_number == " ":
            print("Enter a credit card number not nothing.")
            frfr(0.5)
        else: break
    return cc_number    

def clean_credit_card(credit_card_number="",dividers=set()):
    dividers.update([" ","-"])
    for divider in dividers:
        credit_card_number = credit_card_number.replace(divider,"")

    print(credit_card_number)

def Luhns_Algorithm(credit_card_number):
    """
    Algorithm Steps:
    1. Starting from the rightmost digit (excluding check digit), move left.
    2. Double every second digit.
    3. If doubling results in a number > 9, add its digits together (e.g., 16 -> 1+6 = 7).
    4. Add up all digits (including untouched ones).
    5. If total is divisible by 10, number is valid.
    
    Args:
        number (str): The number to validate as a string.
                     Example: "7992739871"
    
    Returns:
        bool: True if number is valid, False otherwise.
    
    Examples:
        >>> validate_number("79927398713")
        True
        
        Step-by-step example using "7992739871":
        1. Starting from right: 7992739871
        2. Double every second digit from right:
           Original:  7 9 9 2 7 3 9 8 7 1
           Doubled:   7 18 9 4 7 6 9 16 7 2
        3. Sum digits of numbers > 9:
           After sum: 7 9 9 4 7 6 9 7 7 2
        4. Add all digits: 7+9+9+4+7+6+9+7+7+2 = 67
        5. Check if sum (67) is divisible by 10 (it's not, so number is invalid)
    
    Note:
        - Input should be a string of digits
        - Spaces and non-numeric characters should be removed before passing to function
        - Returns False for empty string or invalid input
    """
    pass

clean_credit_card("123123-1231432 13123- ____1123123",{"_"})