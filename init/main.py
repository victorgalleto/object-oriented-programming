import csv

class Item:

    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0): #call actions instantly

        # Run validations to the recieved arguments
        assert price > 0, f'Price {price} is not greater than zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity #they were already initialized

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        # Context management
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)


    def __repr__(self):
        # Important to maintain the same way the instances are declared
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item('Phone', 100, 1)
item1.calculate_total_price()

item2 = Item('Laptop', 1000, 3)
item2.pay_rate = 0.7

Item.instantiate_from_csv()