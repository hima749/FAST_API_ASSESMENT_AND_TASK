# FastAPI Product Management System

This project is a RESTful API built using FastAPI for managing products, customer feedback, and bulk orders. It demonstrates backend development concepts including API design, data validation, and business logic implementation.

## 📌 Features Implemented

### 1. Product Filtering API

* Filter products based on:

  * Minimum price
  * Maximum price
  * Category

### 2. Product Price Retrieval

* Get the price of a product using product ID

### 3. Customer Feedback System

* Submit feedback for products
* Includes validation for:

  * Name
  * Rating (1–5)
  * Optional comments

### 4. Product Summary API

* Total number of products
* In-stock vs out-of-stock count
* Most expensive and cheapest product
* Available categories

### 5. Bulk Order Processing

* Place bulk orders with multiple items
* Validates stock availability
* Calculates total cost
* Handles failed and successful orders

## 🧠 Concepts Used

* FastAPI framework
* REST API development
* Pydantic models for data validation
* Query parameters & path parameters
* List comprehensions and filtering
* Business logic implementation

## 📂 File

* `main.py` → contains all API endpoints and logic 

## ▶️ How to Run

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Then open:

```
http://127.0.0.1:8000/docs
```

## 🚀 Outcome

Developed a fully functional API system capable of handling product management, feedback collection, and bulk order processing using FastAPI.
