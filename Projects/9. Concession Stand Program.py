concession_menu = {
        "Popcorn": 700.00,
        "Soda": 350.00,
        "Nachos": 650.00,
        "Hot Dog": 500.00,
        "Pretzel": 300.00,
        "M&Ms": 200.00,
        "Skittles": 220.00,
        "Twizzlers": 230.00,
        "Ice Cream": 280.00,
        "Slushie": 370.00,
        "Pizza Slice": 550.00,
        "Chicken Tenders": 700.00,
        "French Fries": 320.00,
        "Mozzarella Sticks": 450.00,
        "Onion Rings": 330.00,
        "Bottled Water": 150.00,
        "Coffee": 240.00,
        "Tea": 180.00,
        "Milkshake": 480.00,
        "Cheeseburger": 750.00,
        "Veggie Burger": 680.00,
        "Churros": 310.00,
        "Soft Pretzel Bites": 340.00,
        "Chicken Wings": 720.00,
        "Fruit Snacks": 260.00,
        "Trail Mix": 290.00
    }
    
concession_menu_lower = {k.lower(): v for k, v in concession_menu.items()}
    
def display_menu(concession_menu=dict):
    # Create a dictionary of the concession stand menu
    
    print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ Menu ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
    # Display the menu
    for i, (food, price) in enumerate(concession_menu.items()):
        print(f"{i}. {food} {'-' * (40 - len(food) - len(str(i)))} Rs.{price}")

def ask_user_input(concession_menu_lower=dict):
    user_items = []
    while True:
        user_input = input("Which food item would you like to order?(q to quit)\n: ").lower()
        if user_input not in concession_menu_lower.keys() and user_input not in ["q","quit"]:
            print("Try Again!")
        elif user_input in concession_menu_lower.keys():
            print(f"{user_input} has been added to the list.")
            user_items.append(user_input)
        elif user_input in ["q","quit"]:
            return user_items

def add_items_and_calculate_total(user_items=list,menu=dict):
    total_price = 0
    for i in user_items:
        total_price += menu[i]
    print(f"Total price: Rs.{total_price:.2f}")

display_menu(concession_menu)
user_items = ask_user_input(concession_menu_lower)
add_items_and_calculate_total(user_items,concession_menu_lower)
