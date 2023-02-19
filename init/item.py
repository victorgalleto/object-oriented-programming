import csv

class Item:


    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0): #call actions instantly

        # Run validations to the recieved arguments
        assert price > 0, f'Price {price} is not greater than zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'
        
        # Assign to self object
        self.__name = name   # Now it's impossible to change the name and also access it with underscore
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:   
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity #they were already initialized

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    # Access in the Class level only
    def instantiate_from_csv(cls):
        # Context management "with"
        with open(r'C:\Users\Galleto\Web_Projects\object-oriented-programming\init\items.csv') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    # Static methods are not focused in managing structure data
    # as seen in Class methods
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
   
    def __repr__(self):
        
        # Important to maintain the same way the instances are declared. Good practice for documentations
        # Shows in the console in a more friendly way
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

