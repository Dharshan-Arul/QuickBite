# 🍕 QuickBite — Food Ordering System

A Python console-based food ordering system inspired by Swiggy/Zomato.
Built for beginners to learn Python and use in interviews.

---

## 📁 Project Structure

```
QuickBite/
│
├── main.py       ← Run this file to start
├── user.py       ← Login & Register
├── menu.py       ← Menu display & management
├── cart.py       ← Cart operations
├── order.py      ← Billing & order history
├── admin.py      ← Admin panel
├── README.md     ← This file
└── data/         ← Auto-created folder
    ├── users.json     ← Stores user data
    ├── menu.json      ← Stores menu items
    └── orders.json    ← Stores all orders
```

---

## ▶️ How to Run

1. Open VS Code
2. Open the `QuickBite` folder
3. Open terminal → `View → Terminal`
4. Type:
```
python main.py
```

---

## ✅ Features

### Customer
- Register & Login with phone + password
- Browse menu by category
- Add / Remove items from cart
- Apply coupon codes (WELCOME10, SAVE20, FLAT50)
- Place order with GST bill
- View order history

### Admin
- Password: `admin123`
- View all orders & total revenue
- Add / Remove menu items
- Update item prices

---

## 🐍 Python Concepts Used

| Concept | Where Used |
|--------|-----------|
| Functions | Every module |
| OOP (dict/list) | Menu, Cart, Orders |
| File Handling | JSON read/write |
| Loops | Menus, cart display |
| Conditions | Login, coupon, choices |
| Modules & Import | All files |
| datetime | Order timestamp |
| os module | File/folder creation |

---

> "I built QuickBite, a food ordering system inspired by Swiggy.
> It has customer login, menu browsing, cart management, coupon system,
> GST billing, and an admin panel — all using Python with JSON file storage.
> It covers OOP concepts, file handling, modular programming, and real-world logic."

---

## 🔑 Admin Password
```
admin123
```
