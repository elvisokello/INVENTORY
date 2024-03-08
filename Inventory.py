from datetime import datetime

class Product:
    def __init__(self, product_id, name, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.quantity_in_stock = quantity_in_stock

    def calculate_value(self):
        pass

class SimpleProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price

    def calculate_value(self):
        return self.quantity_in_stock * self.unit_price

class PerishableProduct(SimpleProduct):
    def __init__(self, product_id, name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id, name, quantity_in_stock, unit_price)  # added unit_price here
        self.expiry_date = expiry_date

    def calculate_value(self):
        remaining_shelf_life = (self.expiry_date - datetime.now()).days
        if remaining_shelf_life > 0:
            discount = remaining_shelf_life / 31
            return (1 - discount) * self.quantity_in_stock * self.unit_price
        else:
            return 0

class DigitalProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price

    def calculate_value(self):
        pass

product_id = input("Enter product_id: ")
name = input("Enter name: ")
quantity_in_stock = int(input("Enter Quantity_in_stock: "))
unit_price = float(input("Enter unit_price: "))
expiry_date = datetime.strptime(input("Enter expiry_date (yyyy-mm-dd): "), "%Y-%m-%d")

perishable_product = PerishableProduct(product_id, name, quantity_in_stock, unit_price, expiry_date)
print("Shelf life value: ", perishable_product.calculate_value())
