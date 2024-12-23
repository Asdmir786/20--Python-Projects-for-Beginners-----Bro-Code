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

print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ Menu ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")

for food,price in concession_menu.items():
    print(f"{food} {'-' * (40 - len(food) - 1)} Rs.{price}")
