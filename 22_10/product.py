class Product(object):

    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def __str__(self):
        return f"product: {self.color} {self.name} " \
               f"price: {self.price}"

    def __repr__(self):
        return f"product {self.name} - {self.price}"

    def __eq__(self, other):
        if self.color == other.color and self.price == other.price:
            return True
        else:
            return False

    def __add__(self, other):
        return self.price + other.price