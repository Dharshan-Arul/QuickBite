# ============================
#         admin.py
#   Admin Panel
# ============================

import json
import os
from menu import add_menu_item, remove_menu_item, update_price
from order import load_orders

ADMIN_PASSWORD = "admin123"


def view_all_orders():
    """Admin: View all orders"""
    orders = load_orders()
    if not orders:
        print("\n📭 No orders yet!")
        return

    print("\n============================")
    print("       📋 ALL ORDERS")
    print("============================")
    total_revenue = 0
    for order in orders:
        print(f" {order['order_id']} | {order['customer_name']:<15} | ₹{order['total']} | {order['date_time']}")
        total_revenue += order["total"]

    print("============================")
    print(f" Total Orders  : {len(orders)}")
    print(f" Total Revenue : ₹{round(total_revenue, 2)}")
    print("============================")


def admin_login():
    """Admin login"""
    print("\n============================")
    print("      🔐 ADMIN LOGIN")
    print("============================")
    password = input("Enter admin password: ")
    if password == ADMIN_PASSWORD:
        print("✅ Admin access granted!")
        return True
    else:
        print("❌ Wrong password!")
        return False


def admin_panel():
    """Admin panel menu"""
    if not admin_login():
        return

    while True:
        print("\n============================")
        print("       ⚙️  ADMIN PANEL")
        print("============================")
        print("1. View All Orders")
        print("2. Add Menu Item")
        print("3. Remove Menu Item")
        print("4. Update Item Price")
        print("5. Back to Main Menu")

        choice = input("\nEnter choice (1-5): ")

        if choice == "1":
            view_all_orders()
        elif choice == "2":
            add_menu_item()
        elif choice == "3":
            remove_menu_item()
        elif choice == "4":
            update_price()
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice!")
