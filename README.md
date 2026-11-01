# Shopping-Cart-Billing-System
A Shopping Cart Billing System that allows customers to place orders, records customer information and purchased products, calculates the total bill, and generates a printable receipt.
# 🛒 Shopping Cart Billing System

A Python-based Shopping Cart Billing System that collects customer information, manages product purchases, calculates bills, applies discounts, and handles payment processing.

## 📌 Project Overview

This project is a console-based billing application developed using Python. It allows customers to select products, enter quantities, and calculate their bills automatically.

The system also provides discount offers based on the purchase amount and customer age, applies service charges for card payments, and calculates the remaining change.

## ✨ Features

- **Customer Information:** Collects customer name, age, city, and customer ID.
- **Product Catalog:** Displays available products and their prices.
- **Product Selection:** Allows customers to select up to five products.
- **Quantity Management:** Calculates product costs based on selected quantities.
- **Automatic Bill Calculation:** Calculates the total purchase amount.
- **Purchase Discounts:**
  - 5% discount on purchases of 2,000 or more.
  - 10% discount on purchases of 5,000 or more.
  - 15% discount on purchases of 10,000 or more.
- **Senior Citizen Discount:** Additional 5% discount for customers aged 60 or above.
- **Payment Methods:** Supports Cash and Card payments.
- **Card Service Charges:** Applies a 2% service charge to card payments.
- **Payment Calculation:** Checks the amount paid and calculates the remaining change.
- **Customer Classification:** Categorizes customers into Regular, Silver, Gold, and Premium based on their purchase amount.
- **Final Report:** Organizes customer information, product details, and billing information in a nested Python dictionary.

## 🛍️ Available Products

| Product | Price |
|---|---:|
| Milk | Rs. 200 |
| Toothpaste | Rs. 100 |
| Bread | Rs. 150 |
| Sugar | Rs. 80 |
| Cold Drink | Rs. 180 |
| Besan | Rs. 150 |
| Rice | Rs. 400 |
| Maggie | Rs. 50 |

## 🛠️ Technologies Used

- Python 3
- Dictionaries
- Lists
- For Loops
- Conditional Statements (if, elif, else)
- User Input and Type Conversion
- Arithmetic Operations
- Nested Dictionaries

## ▶️ How to Run

1. Clone this repository:

   ```bash
   git clone YOUR-REPOSITORY-SSH-URL
   ```

2. Navigate to the project directory:

   ```bash
   cd SHOPPING-CART-BILLING-SYSTEM
   ```

3. Run the Python file:

   ```bash
   python main.py
   ```

## 🚀 Future Improvements

- Fix and improve total bill calculation for multiple products.
- Store all purchased products and quantities in the final report.
- Add proper input validation and error handling.
- Generate and print formatted customer receipts.
- Save customer billing records in a file.
- Add a graphical user interface (GUI).

## 👨‍💻 Author

**Shamoon Gill**

A beginner Python developer learning programming, Git, and GitHub through practical projects.

---

*This project was created as part of my Python programming learning journey.*
