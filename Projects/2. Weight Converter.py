# Pounds = KiloGrams * 2.20462
# KiloGrams = Pounds / 2.20462

CONSTANT_FOR_CALCULATIONS = 2.20462

def get_input(prompt=""):
    while True:
        number = input(prompt)
        try:
            number = float(number)
            if number > 0:
                return number
            else: print("Not 0 Plj")
        except ValueError:
            print("Please enter a valid number.")

def get_unit(prompt_output="",input_number=0):
    if input_number > 1:
        prompt_output = "What is the unit of the Number you provided(kgs,lbs): "
    elif input_number == 1:
        prompt_output = "What is the unit of the Number you provided(kg,lb): "
    while True: 
        unit = input(prompt_output)
        if input_number > 1 and unit in ["kgs","lbs"]:
            return unit
        elif input_number == 1 and unit in ["kg","lb"]:
            return unit
        else:
            if input_number > 1:
                print("Enter kgs/lbs.")
            elif input_number == 1:
                print("Enter kg/lb.")
                

def calculation(number_input=0,unit_original=""):
    if unit_original in ["kgs","kg"]:
        number_output = number_input * CONSTANT_FOR_CALCULATIONS
        if number_output > 1: 
            return f"{number_output:.4f} lbs"
        elif number_output == 1: 
            return f"{number_output:.4f} lb"
    elif unit_original in ["lb","lbs"]:
        number_output = number_input / CONSTANT_FOR_CALCULATIONS  
        if number_output > 1: return f"{number_output:.4f} kgs"
        elif number_output == 1: return f"{number_output:.4f} kg"
    
    return number_output

def main():
    main_number = get_input("Give a Number in Kilogram or in Pounds(kgs/kg/lb/lbs): ")
    main_number_unit = get_unit("",main_number)
    output = calculation(main_number,main_number_unit)

    print(f"{main_number} {main_number_unit} = {output}")

main()