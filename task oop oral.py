from abc import ABC, abstractmethod


# =========================
# Abstract Base Class
# =========================

class MenuItem(ABC):

    def __init__(self, item_id, name, price, available=True):

        self.__item_id = item_id
        self.__name = name
        self.__price = price
        self.__available = available

    # ---------- Getters ----------

    def get_id(self):
        return self.__item_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def is_available(self):
        return self.__available

    # ---------- Setters ----------

    def set_price(self, new_price):

        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

    def set_availability(self, status):

        if isinstance(status, bool):
            self.__available = status
        else:
            print("Availability must be True or False")

    # ---------- Abstract Methods ----------

    @abstractmethod
    def calculate_final_price(self):
        pass

    @abstractmethod
    def display_info(self):
        pass


# =========================
# Food Class
# =========================

class FoodItem(MenuItem):

    def __init__(self, item_id, name, price, allergy_warning):

        super().__init__(item_id, name, price)

        self.allergy_warning = allergy_warning

    def calculate_final_price(self):

        service_fee = self.get_price() * 0.15

        return self.get_price() + service_fee

    def display_info(self):

        print(f"[Food] ID: {self.get_id()} | "
              f"{self.get_name()} | "
              f"Price: ${self.get_price()} | "
              f"Warning: {self.allergy_warning}")


# =========================
# Beverage Class
# =========================

class Beverage(MenuItem):

    def __init__(self, item_id, name, price, size):

        super().__init__(item_id, name, price)

        self.size = size

    def calculate_final_price(self):

        happy_hour_discount = self.get_price() * 0.50

        sugar_tax = self.get_price() * 0.10

        return self.get_price() - happy_hour_discount + sugar_tax

    def display_info(self):

        print(f"[Drink] ID: {self.get_id()} | "
              f"{self.get_name()} | "
              f"Price: ${self.get_price()} | "
              f"Size: {self.size}")


# =========================
# Customer Order
# =========================

class CustomerOrder:

    def __init__(self):

        self.items = []

    def add_item(self, item):

        self.items.append(item)

        print(f"{item.get_name()} added successfully!")

    def view_order(self):

        if not self.items:
            print("Order is empty!")
            return

        print("\n===== CURRENT ORDER =====")

        for item in self.items:

            print(f"{item.get_name()} - ${item.get_price()}")

    def print_receipt(self):

        if not self.items:
            print("No items in order!")
            return

        print("\n========== FINAL RECEIPT ==========")

        total = 0

        for item in self.items:

            final_price = item.calculate_final_price()

            total += final_price

            print(f"{item.get_name()} --> ${final_price:.2f}")

        print("-----------------------------------")

        print(f"TOTAL = ${total:.2f}")


# =========================
# Create Menu
# =========================

menu = [

    FoodItem(1, "Burger", 100, "Contains Gluten"),
    FoodItem(2, "Pizza", 150, "Contains Cheese"),

    Beverage(3, "Cola", 50, "Medium"),
    Beverage(4, "Coffee", 70, "Large")
]

# =========================
# Main Program
# =========================

order = CustomerOrder()

while True:

    print("\n====== RESTAURANT SYSTEM ======")

    print("1. View Menu")
    print("2. Add Item to Order")
    print("3. View Current Order")
    print("4. Print Receipt")
    print("5. Exit")

    try:

        choice = int(input("Enter your choice: "))

        # =========================
        # View Menu
        # =========================

        if choice == 1:

            print("\n========== MENU ==========")

            for item in menu:

                item.display_info()

        # =========================
        # Add Item
        # =========================

        elif choice == 2:

            item_id = int(input("Enter item ID: "))

            found = False

            for item in menu:

                if item.get_id() == item_id:

                    order.add_item(item)

                    found = True

                    break

            if not found:

                print("Item not found!")

        # =========================
        # View Order
        # =========================

        elif choice == 3:

            order.view_order()

        # =========================
        # Print Receipt
        # =========================

        elif choice == 4:

            order.print_receipt()

        # =========================
        # Exit
        # =========================

        elif choice == 5:

            print("Thank you for using the system!")

            break

        else:

            print("Invalid choice!")

    except ValueError:

        print("Please enter a valid number!")