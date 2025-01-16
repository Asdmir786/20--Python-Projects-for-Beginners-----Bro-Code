import time
import os
    
def frfr(time_in_seconds_for_sleep):
    time.sleep(time_in_seconds_for_sleep)
    os.system("cls")
    
def get_credit_card_number():
    while True:
        cc_number = input("Enter your credit card number (only enter space or - for seperators): ").strip()
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
    return credit_card_number

def Luhns_Algorithm(credit_card_number=""):
    credit_card_number = list(map(int,credit_card_number))
    
    print(f"Length:{len(credit_card_number)} \nOriginal List: {credit_card_number}")    
    
    for index,number in enumerate(credit_card_number, start=1):
        if index % 2 == 0:
            number *= 2
        
        if number > 9:
            number -= 9

        credit_card_number[index-1] = number
        
    print(f"Length:{len(credit_card_number)} \nList After Multiplying: {credit_card_number}")   
    
    sum_of_ccn = sum(credit_card_number)
    
    print(f"Sum of All Numbers in the list: {sum_of_ccn}") 
    
    if sum_of_ccn % 10 == 0:
        print("Fr Fr Your Credit Card Valid becuz Luhn's Algorithm said so.")
    else:
        print("Nice try diddy.")
    
def main():
    ccn = get_credit_card_number()        

    cleaned_ccn = clean_credit_card(ccn)

    Luhns_Algorithm(cleaned_ccn)

if __name__ == "__main__":
    main()