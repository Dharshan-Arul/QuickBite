# ============================
#         order.py
#   Handles Orders & Billing
# ============================

import json
import os
from datetime import datetime
from cart import view_cart, get_cart, clear_cart

ORDERS_FILE = "data/orders.json"
GST_RATE = 0.05  # 5% GST

COUPONS = {
    "WELCOME10": 10,   # 10% off
    "SAVE20": 20,      # 20% off
    "FLAT50": 50,      # ₹50 flat off
}


def load_orders():
    """Load all orders from file"""
    if not os.path.exists(ORDERS_FILE):
        return []
    with open(ORDERS_FILE, "r") as f:
        return json.load(f)


def save_order(order):
    """Save a new order to file"""
    orders = load_orders()
    orders.append(order)
    with open(ORDERS_FILE, "w") as f:
        json.dump(orders, f, indent=4)


def apply_coupon(subtotal):
    """Apply coupon and return discount amount"""
    print("\nAvailable Coupons: WELCOME10 | SAVE20 | FLAT50")
    coupon = input("Enter coupon code (or press Enter to skip): ").strip().upper()

    if not coupon:
        return 0, ""

    if coupon not in COUPONS:
        print("❌ Invalid coupon!")
        return 0, ""

    discount_val = COUPONS[coupon]

    # Percentage based
    if coupon in ["WELCOME10", "SAVE20"]:
        discount = round(subtotal * discount_val / 100, 2)
        print(f"✅ Coupon applied! {discount_val}% off → -₹{discount}")
    else:
        discount = min(discount_val, subtotal)  # can't exceed subtotal
        print(f"✅ Coupon applied! Flat -₹{discount}")

    return discount, coupon


def place_order(customer):
    """Place order, generate bill, save to file"""
    cart = get_cart()
    if not cart:
        print("\n❌ Your cart is empty! Add items first.")
        return

    subtotal = view_cart()
    if subtotal == 0:
        return

    # Apply coupon
    discount, coupon_used = apply_coupon(subtotal)
    discounted = subtotal - discount
    gst = round(discounted * GST_RATE, 2)
    total = round(discounted + gst, 2)

    # Generate order ID
    orders = load_orders()
    order_id = f"QB{1001 + len(orders)}"
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M")

    # Print Bill
    print("\n")
    print("=" * 35)
    print("        🍕 QuickBite")
    print("     Food Ordering System")
    print("=" * 35)
    print(f" Order ID  : {order_id}")
    print(f" Customer  : {customer['name']}")
    print(f" Phone     : {customer['phone']}")
    print(f" Date/Time : {date_time}")
    print("-" * 35)
    for item in cart:
        item_total = item["price"] * item["qty"]
        print(f" {item['name'][:20]:<20} x{item['qty']}  ₹{item_total}")
    print("-" * 35)
    print(f" Subtotal  :           ₹{subtotal}")
    if discount > 0:
        print(f" Discount  :          -₹{discount}  ({coupon_used})")
    print(f" GST (5%)  :           ₹{gst}")
    print(f" TOTAL     :           ₹{total}")
    print("=" * 35)
    print("   ✅ Order Placed Successfully!")
    print("   🚴 Estimated delivery: 30 mins")
    print("=" * 35)

    # Save order
    order = {
        "order_id": order_id,
        "customer_name": customer["name"],
        "customer_phone": customer["phone"],
        "items": cart.copy(),
        "subtotal": subtotal,
        "discount": discount,
        "coupon": coupon_used,
        "gst": gst,
        "total": total,
        "date_time": date_time
    }
    save_order(order)
    clear_cart()


def view_order_history(customer):
    """Show past orders of a customer"""
    orders = load_orders()
    my_orders = [o for o in orders if o["customer_phone"] == customer["phone"]]

    if not my_orders:
        print("\n📭 No past orders found!")
        return

    print("\n============================")
    print("      📦 ORDER HISTORY")
    print("============================")
    for order in my_orders:
        print(f"\n Order ID : {order['order_id']}")
        print(f" Date     : {order['date_time']}")
        for item in order["items"]:
            print(f"   - {item['name']} x{item['qty']}")
        print(f" Total    : ₹{order['total']}")
        print(" " + "-" * 28)
