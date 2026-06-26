# ============================
#         cart.py
#   Handles Cart Operations
# ============================

from menu import show_menu, get_item

# Cart stored as a list of dicts
cart = []


def add_to_cart():
    """Add item to cart"""
    show_menu()
    try:
        item_id = input("\nEnter item ID to add: ").strip()
        item = get_item(item_id)
        if not item:
            print("❌ Invalid item ID!")
            return
        qty = int(input(f"Enter quantity for {item['name']}: "))
        if qty <= 0:
            print("❌ Quantity must be at least 1!")
            return

        # Check if item already in cart
        for c in cart:
            if c["item_id"] == item_id:
                c["qty"] += qty
                print(f"✅ {item['name']} quantity updated to {c['qty']}!")
                return

        cart.append({
            "item_id": item_id,
            "name": item["name"],
            "price": item["price"],
            "qty": qty
        })
        print(f"✅ {item['name']} x{qty} added to cart!")

    except ValueError:
        print("❌ Please enter a valid number!")


def view_cart():
    """Display current cart"""
    if not cart:
        print("\n🛒 Your cart is empty!")
        return 0

    print("\n============================")
    print("         🛒 CART")
    print("============================")
    print(f"{'No':<4} {'Item':<25} {'Qty':<5} {'Price'}")
    print("-" * 45)
    total = 0
    for i, item in enumerate(cart, 1):
        item_total = item["price"] * item["qty"]
        print(f"{i:<4} {item['name']:<25} x{item['qty']:<4} ₹{item_total}")
        total += item_total

    print("-" * 45)
    print(f"{'Subtotal':<35} ₹{total}")
    print("============================")
    return total


def remove_from_cart():
    """Remove item from cart"""
    if not cart:
        print("\n🛒 Cart is already empty!")
        return
    view_cart()
    try:
        choice = int(input("\nEnter item number to remove (0 to cancel): "))
        if choice == 0:
            return
        if 1 <= choice <= len(cart):
            removed = cart.pop(choice - 1)
            print(f"✅ {removed['name']} removed from cart!")
        else:
            print("❌ Invalid choice!")
    except ValueError:
        print("❌ Please enter a valid number!")


def clear_cart():
    """Empty the cart"""
    cart.clear()


def get_cart():
    """Return cart items"""
    return cart
