# ============================
#         main.py
#   QuickBite - Entry Point
# ============================

import os
from user import user_menu
from menu import show_menu
from cart import add_to_cart, view_cart, remove_from_cart
from order import place_order, view_order_history
from admin import admin_panel


def create_data_folder():
    """Create data folder if not exists"""
    if not os.path.exists("data"):
        os.makedirs("data")


def customer_menu(user):
    """Main menu for logged-in customer"""
    while True:
        print(f"\n============================")
        print(f"  👋 Hello, {user['name']}!")
        print(f"============================")
        print("1. 🍽️  View Menu")
        print("2. ➕  Add to Cart")
        print("3. 🛒  View Cart")
        print("4. ➖  Remove from Cart")
        print("5. ✅  Place Order")
        print("6. 📦  Order History")
        print("7. 🚪  Logout")

        choice = input("\nEnter choice (1-7): ")

        if choice == "1":
            show_menu()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            remove_from_cart()
        elif choice == "5":
            place_order(user)
        elif choice == "6":
            view_order_history(user)
        elif choice == "7":
            print(f"\n👋 Goodbye, {user['name']}! See you soon!")
            break
        else:
            print("❌ Invalid choice! Try again.")


def main():
    """Main program start"""
    create_data_folder()

    print("\n" + "=" * 35)
    print("       🍕 Welcome to")
    print("         QuickBite!")
    print("   Food Ordering System")
    print("=" * 35)

    while True:
        print("\n1. Customer Login / Register")
        print("2. Admin Panel")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ")

        if choice == "1":
            user = user_menu()
            if user:
                customer_menu(user)

        elif choice == "2":
            admin_panel()

        elif choice == "3":
            print("\n🍕 Thank you for using QuickBite! Goodbye!\n")
            break

        else:
            print("❌ Invalid choice!")


# --- Start Program ---
if __name__ == "__main__":
    main()
