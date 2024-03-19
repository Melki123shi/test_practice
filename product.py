class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculateTotal(self):
        if self.price < 0 or self.quantity < 0:
            raise ValueError
        return self.price * self.quantity
    



