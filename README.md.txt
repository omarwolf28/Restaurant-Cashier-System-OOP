# 🍽️ Restaurant Cashier System

A simple terminal-based restaurant cashier system built using Python and Object-Oriented Programming (OOP) concepts.

---

# 📌 Features

- View restaurant menu
- Add food and beverages to customer order
- View current order
- Print final receipt
- Apply taxes and discounts automatically
- Error handling for invalid inputs
- Interactive terminal interface

---

# 🧠 OOP Concepts Used

This project demonstrates the following OOP principles:

- Abstraction
- Inheritance
- Encapsulation
- Polymorphism

---

# 🏗️ Project Structure

```text
restaurant-cashier-system/
│
├── main.py
├── README.md
```

---

# 🍔 Menu Item Types

## Food Items
- Include allergy warnings
- Add 15% service fee

## Beverage Items
- Include size information
- Apply Happy Hour discount
- Apply sugar tax

---

# ▶️ How to Run

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/restaurant-cashier-system.git
```

---

## 2. Open the project folder

```bash
cd restaurant-cashier-system
```

---

## 3. Run the program

```bash
python main.py
```

---

# 🖥️ Example System Menu

```text
1. View Menu
2. Add Item to Order
3. View Current Order
4. Print Receipt
5. Exit
```

---

# ✅ Example Concepts in the Code

## Encapsulation

Sensitive data like price is protected using private variables and getters/setters.

```python
self.__price
```

---

## Inheritance

```python
class FoodItem(MenuItem)
class Beverage(MenuItem)
```

---

## Polymorphism

Each item has its own implementation of:

```python
calculate_final_price()
```

---

# 👨‍💻 Author

Created as an OOP Programming Project using Python.