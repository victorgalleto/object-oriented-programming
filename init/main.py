class Item:

    pay_rate = 0.8 # The pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity=0): #call actions instantly
        
        # Run validations to the recieved arguments
        assert price > 0, f'Price {price} is not greater than zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity #they were already initialized

item1 = Item('Phone', 100, 1)
item1.calculate_total_price()

item2 = Item('Laptop', 1000, 3)

print(Item.pay_rate)