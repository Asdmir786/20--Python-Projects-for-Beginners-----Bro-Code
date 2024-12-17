
def get_input(prompt=""): # no str() because of difficulty to understand
    while True:
        number = input(prompt) # Enter Your Number.
        try:
            number = float(number)
            if number.is_integer():
                number = int(number)
            return number
        except ValueError:
            try:
                number = int(number)
                return number
            except ValueError:
                print("Please enter a valid number.")

def get_operator(prompt="Enter One of the Operators (+,-,/,*): "):
    while True:
        global operator
        operator = input(prompt)
        if operator in ["-","+","*","/"]:
            return operator
        else:
            print("Write the correct operator. ")

def phull_level_calculation(n1,n2,arithmetic_operator):
    match arithmetic_operator:
        case "+":
            result = n1+n2
            return result
        case "-":
            result = n1-n2
            return result
        case "/":
            result = n1/n2
            return result
        case "*":
            result = n1*n2
            return result
            
def main():
    n1 = get_input("Enter Number #1: ")        
    n2 = get_input("Enter Number #2: ")        
    operator = get_operator()
    print(f"{n1} {operator} {n2} = {phull_level_calculation(n1,n2,operator)}")
    
main()