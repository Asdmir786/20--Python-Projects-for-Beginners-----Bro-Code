#  °F = (°C × 9/5) + 32
#  °C = (°F − 32) x 5/9    

def get_number_and_unit(prompt="Enter you Number with it's unit (e.g. 45 C,182 F, etc): "):
    while True:
        input_data = input(prompt).strip().split()
        if len(input_data) == 2:
            break
        else:
            print("Look, here's the pattern: {Number} {Unit = F | C}, Simple.")

    value,unit = input_data

    if "." in value:
        value = float(value)
    else: value = int(value)
    
    unit = unit.upper().strip()
    
    return value, unit

def calculation(value,unit_original):
    if unit_original == "F":
        converted_value = (value-32)*(5/9)
        return converted_value,"C"
    elif unit_original == "C":
        converted_value = (value*(9/5)+32)
        return converted_value,"F"
    
def main():
    number,unit = get_number_and_unit()
    result_number,result_unit = calculation(number,unit)
    result_number = str(result_number)
    if "." in result_number:
        result_number = float(result_number)
    else: result_number = int(f"{result_number}")
    print(f"{number}° {unit} is {result_number}° {result_unit}")

main()