# FastAPI Advanced E-commerce System

This project is a comprehensive RESTful API built using FastAPI that simulates an advanced e-commerce backend system. It includes cart management, order processing, product search, sorting, and pagination features.

## 📌 Features Implemented

### 🛒 Cart System

* Add products to cart
* Update quantity automatically
* Remove items from cart
* View cart with total price

### 📦 Checkout & Orders

* Place orders with customer details
* Auto-generate order IDs
* Store and retrieve order history

### 🔍 Product Search

* Search products using keywords
* Case-insensitive matching

### ↕️ Product Sorting

* Sort products by:

  * Price
  * Name
* Supports ascending and descending order

### 📄 Pagination

* Paginate product list
* Control page number and limit

### 🔎 Order Search

* Search orders by customer name

### 📊 Category-Based Sorting

* Sort products by category and price

### 🧠 Advanced Browsing API

* Combines:

  * Search
  * Sorting
  * Pagination
* Single endpoint for flexible product browsing

### 🎁 Bonus Feature

* Pagination for orders

---

## 🧠 Concepts Used

* FastAPI framework
* REST API design
* Pydantic models
* Query parameters & validation
* Exception handling (`HTTPException`)
* Sorting & filtering logic
* Pagination techniques
* Data structures (lists & dictionaries)

---

## 📂 File

* `main.py` → contains full API implementation 

---

## ▶️ How to Run

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🚀 Outcome

Developed a fully functional advanced e-commerce backend system with powerful features like search, sorting, pagination, and order management using FastAPI.

---

## 💡 Highlights

* Real-world backend logic
* Scalable API design
* Clean and modular implementation
* Industry-relevant project
