fastapi-day2-assignment
This repository contains the solutions for the FastAPI Day 2 Practice Tasks from the internship training program.

Project Description
The assignment demonstrates basic API development using FastAPI, including:

Creating GET endpoints
Using query parameters
Handling path parameters
Implementing POST requests
Data validation using Pydantic models
Business logic implementation for API responses
Implemented Endpoints
Filter Products

Endpoint: /products/filter
Filters products based on minimum price, maximum price, and category.
Get Product Price

Endpoint: /products/{product_id}/price
Returns only the name and price of a specific product.
Customer Feedback

Endpoint: /feedback
Accepts customer feedback using a POST request with validation.
Product Summary

Endpoint: /products/summary
Provides summary statistics such as total products, stock availability, most expensive and cheapest products, and categories.
Bulk Order Processing

Endpoint: /orders/bulk
Processes multiple order items, validates product availability, and calculates total cost.
Technologies Used
Python
FastAPI
Uvicorn
Pydantic

How to Run the Project
Install dependencies
pip install fastapi uvicorn

Run the server
uvicorn main:app --reload

Open Swagger UI
http://127.0.0.1:8000/docs

Author
Himanshu Shekhar Singh
