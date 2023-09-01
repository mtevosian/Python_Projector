# Create a class Product with properties name, price, and quantity.
# Create a child class Book that inherits from Product and adds a property author and a method called read that prints information about the book.

class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name, price, quantity, author: str):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        return f"{self.name}, {self.price}, {self.quantity}, {self.author}"


book = Book("Bible", 500, 10000, "Jesus")
book.read()


# Create a class Restaurant with properties name, cuisine, and menu.
# The menu property should be a dictionary with keys being the dish name and values being the price.
# Create a child class FastFood that inherits from Restaurant and adds a property drive_thru (a boolean indicating whether the restaurant has a drive-thru or not)
# and a method called order which takes in the dish name and quantity and returns the total cost of the order.
# The method should also update the menu dictionary to subtract the ordered quantity from the available quantity.
# If the dish is not available or if the requested quantity is greater than the available quantity, the method should return a message indicating that the order cannot be fulfilled.
# Example of usage:

class Restaurant:
    def __init__(self, name: str, cuisine: str, menu: dict):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, name, quantity):
        if name not in menu:
            return 'Dish not available'

        if quantity > menu[name]['quantity']:
            return 'Requested quantity not available'
        else:
            menu[name]['quantity'] -= quantity

        self.total_cost = quantity * (menu[name]['price'])
        return self.total_cost


menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))  # 25
print(mc.order('burger', 15))  # Requested quantity not available
print(mc.order('soup', 5))  # Dish not available
