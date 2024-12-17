def get_email(prompt="Enter email: "):
    email = input(prompt)
    return email

def is_email_valid(email=""):
    if "@" not in email:
        return False
    count = email.count("@")
    if count > 1:
        return False
    else:
        return True
    
def email_parser(email=""):
    username,domain = email.split("@")
    return username,domain

def main():
    while True:
        email = get_email()
        result = is_email_valid(email)
        if result == True:
            break
        else:
            print("Incorrect email!")
            print("Enter the email with this pattern: {username}@{domain} e.g kela@gmail.com")
    
    username,domain = email_parser(email)

    print(f"The username of the email is {username} and the domain is {domain}. ")

main()    