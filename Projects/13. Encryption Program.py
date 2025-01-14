import random
import time
import os

# Original letters and numbers
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

# Create a copy of the original list
letters_shuffled = letters[:]

# Shuffle the copy in place
random.shuffle(letters_shuffled)

ignore_letters = [
    " ", "!", "@", "#", "$", "%", "^", "&", "*", "()", "[]", "{}",":",
    ";", "'", "\"", " |", "\\", ",", "<>", "/", "?", "_", "-", "=","+"
    ]

# Caesar cipher equivalent with shift by 5
caesar_letters_5 = [
    'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D',
    'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    '5', '6', '7', '8', '9', '0', '1', '2', '3', '4'
]

def ask_user_for_encryption():
    while True:
        user_input = input('''
Here's the list of encryption: 
1. Caesar Cipher 
2. Extended Monoalphabetic Substitution Cipher
Enter the encryption number(1,2): ''').strip()
        if user_input not in ["1","2"]:
            print("Invalid Number, Enter the number please.")
            time.sleep(1.5)
            os.system("cls")
        else:
            return int(user_input)

def ask_user_for_text():
    while True:
        user_string = input("Enter you Text: ")

        if user_string == "":
            print("Enter something innit? ")
            time.sleep(1.5)
            os.system("cls")
        else:
            return user_string

def Caesar_Cypher_Encrypt(user_string):
    match_index = []
    user_string = list(user_string)
    encrypted_string = []
    # print(user_string)
    for I in user_string:
        if I in ignore_letters:
            match_index.append(I)
            continue
        match_index.append(letters.index(I))
    
    print(f"match index: {match_index}")
    for I in match_index:
        if I in ignore_letters:
            encrypted_string.append(I)
            continue
        encrypted_string.append(caesar_letters_5[I])
    result = ''.join(encrypted_string)
    print(f" Encrypted String: {result}")
    return result

def Caesar_Cypher_Decrypt(encrypted_string):
    match_index = []
    encrypted_string = list(encrypted_string)
    decrypted_string = []

    for I in encrypted_string:
        if I in ignore_letters:
            match_index.append(I)
            continue
        match_index.append(caesar_letters_5.index(I))
    print(f"match index: {match_index}")
    
    for I in match_index:
        if I in ignore_letters:
            decrypted_string.append(I)
            continue
        decrypted_string.append(letters[I])
    result = ''.join(decrypted_string)
    print(f" Decrypted String: {result}")
    return result
  
def Caesar_Cypher():
    while True:
        eod = input("Do you want to Encrypt or Decrypt(E/D): ").upper().strip()
        if eod not in ["E","D"]:
            print("Enter E or D.")
            time.sleep(0.3)
            os.system("cls")
        else: break
        
    if eod == "E":
        user_text = ask_user_for_text()
        Caesar_Cypher_Encrypt(user_text)
    else: 
        user_text = ask_user_for_text()
        Caesar_Cypher_Decrypt(user_text)
    
def Extended_Monoalphabetic_Substitution_Cipher():
    while True:
        eod = input("Do you want to Encrypt or Decrypt(E/D): ").upper().strip()
        if eod not in ["E","D"]:
            print("Enter E or D.")
            time.sleep(0.3)
            os.system("cls")
        else: break
    
    if eod == "E":
        user_text = ask_user_for_text()
        Extended_Monoalphabetic_Substitution_Cipher_Encrypt(user_text)
    else: 
        user_text = ask_user_for_text()
        Extended_Monoalphabetic_Substitution_Cipher_Decrypt(user_text)

def Extended_Monoalphabetic_Substitution_Cipher_Encrypt(user_input):
    user_input = list(user_input)
    matching_index = []
    encrypted_string = []

    for i in user_input:
        if i in ignore_letters:
            matching_index.append(i)
            continue
        matching_index.append(letters.index(i))
    print(f"WHatever this is: {matching_index}")
    print(f"type: {type(matching_index)}")
    
    for i in matching_index:
        if i in ignore_letters:
            encrypted_string.append(i)
            continue
        encrypted_string.append(letters_shuffled[i])
    result = ''.join(encrypted_string)
    print(f" Decrypted String: {result}")
    return encrypted_string

def Extended_Monoalphabetic_Substitution_Cipher_Decrypt(encrypted_string):
    encrypted_string = list(encrypted_string)
    matching_index = []
    decrypted_string = []

    for i in encrypted_string:
        if i in ignore_letters:
            matching_index.append(i)
            continue
        matching_index.append(letters_shuffled.index(i))
    print(f"WHatever this is: {matching_index}")
    print(f"type: {type(matching_index)}")
    
    for i in matching_index:
        if i in ignore_letters:
            decrypted_string.append(i)
            continue
        decrypted_string.append(letters[i])
    result = ''.join(decrypted_string)
    print(f" Decrypted String: {result}")
    return decrypted_string
    
def main():
    encryption_method = ask_user_for_encryption()
    
    while True:
        if encryption_method == 1:
            Caesar_Cypher()
        else:
            Extended_Monoalphabetic_Substitution_Cipher()
        
        user_choice = input("Do you want to continue or not?(y/n): ").lower().strip()
        if user_choice == 'y':
            continue
        elif user_choice == 'n':
            print("Bye Bye.")
            time.sleep(2)
            os.system("cls")
            exit()
        else:
            print("Enter y or n?")
            time.sleep(0.5)
            os.system("cls")
        
if __name__ == "__main__":
    main()