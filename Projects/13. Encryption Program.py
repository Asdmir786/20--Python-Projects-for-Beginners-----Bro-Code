# Original letters and numbers
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

# Caesar cipher equivalent with shift by 5
caesar_letters = [
    'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D',
    'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    '5', '6', '7', '8', '9', '0', '1', '2', '3', '4'
]

def ask_user_for_encryption():
    while True:
        user_input = input('''
Here's the list of encryption: 
1. Caesar Cipher 
2. Substitution Cipher
(1,2)
''').strip()
        if user_input not in ["1","2"]:
            print("Invalid Number, Enter the number please.")
        else:
            return user_input

def ask_user_for_text(user_input):
    while True:
        if user_input == "1":
            user_string = input("Enter Your Text Innit: ").strip().lower()
        elif user_input == "2":
            user_string = input("Enter you text you bloody: ").strip().lower()

        if user_string == " ":
            print("Enter something innit? ")
        else:
            return user_string

def Caesar_Cypher(user_string):
    pass