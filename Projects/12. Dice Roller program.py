import random

dice_ascii = {
    1: [
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ],
    2: [
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ],
    3: [
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ],
    4: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ],
    5: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ],
    6: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ]
}

def display_dice(total_number_of_dice=1):
    list_of_dice = []
    count = 0
    while count < total_number_of_dice:
        # Check if there are at least two dice left to roll
        if total_number_of_dice - count != 1 and not(total_number_of_dice - count <= 0):  
            random_number = random.randint(1, 6)
            random_number_2 = random.randint(1, 6)
            list_of_dice.append(random_number)
            list_of_dice.append(random_number_2)
            # Print two dice side by side
            for j in range(len(dice_ascii[1])):
                print(f"{dice_ascii[random_number][j]}\t {dice_ascii[random_number_2][j]}")
            count += 2
        else:
            random_number_3 = random.randint(1, 6)
            list_of_dice.append(random_number_3)
            # Print one die
            for j in range(len(dice_ascii[1])):
                print(f"{dice_ascii[random_number_3][j]}")
            count += 1
    print(list_of_dice)
    return list_of_dice

def add_all_dices(list_dice=list):
    sum_of_dices = sum(list_dice)
    print(f"Total: {sum_of_dices}")

def main():
    while True:
        try:
            times_to_roll = int(input("How many Times To Roll The Dice\n: "))
            if times_to_roll <= 0: print("Enter a Number > than 0: ")
            else: break
        except ValueError:
            print("Enter a Number.")
    
    list_of_dice = display_dice(times_to_roll)
    add_all_dices(list_of_dice)

    

if __name__ == "__main__":
    main()