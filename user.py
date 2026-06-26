# ============================
#         user.py
#   Handles Login & Register
# ============================

import json
import os

USERS_FILE = "data/users.json"


def load_users():
    """Load users from file"""
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    """Save users to file"""
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


def register():
    """Register a new user"""
    print("\n============================")
    print("        📝 REGISTER")
    print("============================")
    name = input("Enter your name: ").strip()
    phone = input("Enter phone number: ").strip()
    password = input("Create password: ").strip()

    users = load_users()

    if phone in users:
        print("❌ Phone number already registered! Please login.")
        return None

    users[phone] = {"name": name, "phone": phone, "password": password}
    save_users(users)
    print(f"\n✅ Registration successful! Welcome {name}!")
    return {"name": name, "phone": phone}


def login():
    """Login existing user"""
    print("\n============================")
    print("         🔐 LOGIN")
    print("============================")
    phone = input("Enter phone number: ").strip()
    password = input("Enter password: ").strip()

    users = load_users()

    if phone not in users:
        print("❌ Phone number not found! Please register.")
        return None

    if users[phone]["password"] != password:
        print("❌ Wrong password! Try again.")
        return None

    print(f"\n✅ Welcome back, {users[phone]['name']}!")
    return {"name": users[phone]["name"], "phone": phone}


def user_menu():
    """Show login or register options"""
    while True:
        print("\n============================")
        print("     🍕 QuickBite")
        print("============================")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("\nEnter choice (1-3): ")

        if choice == "1":
            user = login()
            if user:
                return user
        elif choice == "2":
            user = register()
            if user:
                return user
        elif choice == "3":
            return None
        else:
            print("❌ Invalid choice!")
