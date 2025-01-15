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

clean_credit_card("123123-1231432 13123- ____1123123",{"_"})