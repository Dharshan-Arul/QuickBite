# ============================
#         menu.py
#   Handles Menu Display
# ============================

import json
import os

MENU_FILE = "data/menu.json"

# Default menu if no file exists
DEFAULT_MENU = {
    "1": {"name": "Chicken Biryani",       "price": 180, "category": "Rice"},
    "2": {"name": "Veg Fried Rice",         "price": 120, "category": "Rice"},
    "3": {"name": "Paneer Butter Masala",   "price": 150, "category": "Curry"},
    "4": {"name": "Dal Tadka",              "price": 100, "category": "Curry"},
    "5": {"name": "Garlic Bread",           "price": 60,  "category": "Snack"},
    "6": {"name": "French Fries",           "price": 80,  "category": "Snack"},
    "7": {"name": "Pepsi",                  "price": 40,  "category": "Drink"},
    "8": {"name": "Mango Lassi",            "price": 60,  "category": "Drink"},
    "9": {"name": "Chocolate Cake",         "price": 90,  "category": "Dessert"},
    "10": {"name": "Gulab Jamun",           "price": 50,  "category": "Dessert"},
}


def load_menu():
    """Load menu from file, create default if not exists"""
    if not os.path.exists(MENU_FILE):
        save_menu(DEFAULT_MENU)
        return DEFAULT_MENU
    with open(MENU_FILE, "r") as f:
        return json.load(f)


def save_menu(menu):
    """Save menu to file"""
    with open(MENU_FILE, "w") as f:
        json.dump(menu, f, indent=4)


def show_menu():
    """Display full menu"""
    menu = load_menu()
    print("\n============================")
    print("         🍽️  MENU")
    print("============================")
    categories = {}
    for item_id, item in menu.items():
        cat = item["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append((item_id, item))

    for category, items in categories.items():
        print(f"\n  📌 {category}")
        print(f"  {'ID':<5} {'Item':<25} {'Price'}")
        print("  " + "-" * 35)
        for item_id, item in items:
            print(f"  {item_id:<5} {item['name']:<25} ₹{item['price']}")

    print("\n============================")
    return menu


def get_item(item_id):
    """Get a single item by ID"""
    menu = load_menu()
    return menu.get(str(item_id))


def add_menu_item():
    """Admin: Add new item to menu"""
    menu = load_menu()
    print("\n--- Add Menu Item ---")
    new_id = str(max(int(k) for k in menu.keys()) + 1)
    name = input("Item name: ").strip()
    price = int(input("Price: ₹"))
    category = input("Category (Rice/Curry/Snack/Drink/Dessert): ").strip()
    menu[new_id] = {"name": name, "price": price, "category": category}
    save_menu(menu)
    print(f"✅ '{name}' added to menu!")


def remove_menu_item():
    """Admin: Remove item from menu"""
    menu = load_menu()
    show_menu()
    item_id = input("\nEnter item ID to remove: ").strip()
    if item_id in menu:
        removed = menu.pop(item_id)
        save_menu(menu)
        print(f"✅ '{removed['name']}' removed from menu!")
    else:
        print("❌ Item ID not found!")


def update_price():
    """Admin: Update item price"""
    menu = load_menu()
    show_menu()
    item_id = input("\nEnter item ID to update price: ").strip()
    if item_id in menu:
        new_price = int(input(f"New price for {menu[item_id]['name']}: ₹"))
        menu[item_id]["price"] = new_price
        save_menu(menu)
        print(f"✅ Price updated!")
    else:
        print("❌ Item ID not found!")
