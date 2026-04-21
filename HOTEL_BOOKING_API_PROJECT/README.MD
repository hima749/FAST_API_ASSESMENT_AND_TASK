# FastAPI Hotel Booking Management System

This project is a comprehensive RESTful API built using FastAPI for managing hotel rooms and bookings. It simulates a real-world hotel management backend with features like room browsing, booking, filtering, sorting, and checkout operations.

## 📌 Features Implemented

### 🏨 Room Management

* View all rooms with availability
* Add new rooms
* Update room details (price, availability)
* Delete rooms (only if not occupied)

### 🔍 Room Search & Filtering

* Search rooms by keyword
* Filter rooms based on:

  * Room type
  * Price
  * Floor
  * Availability

### ↕️ Sorting & Pagination

* Sort rooms by:

  * Price
  * Floor
  * Type
* Paginate room listings

### 🧠 Advanced Browsing

* Combined API for:

  * Search
  * Sorting
  * Pagination

### 📊 Room Summary

* Total rooms
* Available vs occupied rooms
* Cheapest and most expensive rooms
* Room type distribution

---

### 📅 Booking System

* Create booking with:

  * Guest details
  * Room selection
  * Meal plan options
* Automatic room availability update

### 💰 Pricing & Discounts

* Cost calculated based on:

  * Nights stayed
  * Meal plan (breakfast / all-inclusive)
* Discount applied for early checkout

### 🔄 Booking Operations

* Check-in and check-out functionality
* Track booking status

### 🔎 Booking Search & Sorting

* Search bookings by guest name
* Sort bookings by total cost
* View active bookings

---

## 🧠 Concepts Used

* FastAPI framework
* REST API design
* Pydantic models & validation
* Query parameters
* Sorting, filtering, pagination
* Business logic implementation
* Data structures (lists & dictionaries)

---

## 📂 File

* `main.py` → contains full API implementation 

---

## ▶️ How to Run

```bash id="ff1znx"
pip install fastapi uvicorn
uvicorn main:app --reload
```

Open:

```id="q82kgf"
http://127.0.0.1:8000/docs
```

---

## 🚀 Outcome

Developed a fully functional hotel booking backend system with advanced features like dynamic pricing, filtering, search, and booking lifecycle management.

---

## 💡 Highlights

* Real-world backend system
* Advanced API design
* Clean modular logic
* Industry-relevant project
