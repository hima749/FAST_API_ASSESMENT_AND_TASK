# FastAPI Shopping Cart & Order Management System

This project is a RESTful API built using FastAPI that simulates a basic e-commerce shopping cart and order management system. It allows users to add products to a cart, manage items, and place orders.

## 📌 Features Implemented

### 1. Add to Cart

* Add products using product ID
* Automatically updates quantity if item already exists
* Validates product availability

### 2. View Cart

* Displays all cart items
* Shows total number of items
* Calculates grand total price

### 3. Remove Item from Cart

* Remove a specific product from the cart
* Handles invalid product removal

### 4. Checkout System

* Place order using customer details
* Converts cart items into orders
* Generates order IDs
* Clears cart after checkout

### 5. Order History

* View all placed orders
* Displays total number of orders

## 🧠 Concepts Used

* FastAPI framework
* REST API design
* Pydantic models for request validation
* Path and query parameters
* Exception handling using HTTPException
* List and dictionary operations
* Business logic implementation

## 📂 File

* `main.py` → contains full API logic and endpoints 

## ▶️ How to Run

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

## 🚀 Outcome

Developed a fully functional shopping cart and order management API, demonstrating backend development skills and real-world application logic using FastAPI.

