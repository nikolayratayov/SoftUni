class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def decrease(self, quan):
        if self.quantity >= quan:
            self.quantity -= quan

    def increase(self, quan):
        self.quantity += quan

    def __repr__(self):
        return self.name
    