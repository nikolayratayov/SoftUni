class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, mmls):
        if self.quantity + mmls <= self.size:
            self.quantity += mmls

    def status(self):
        return self.size - self.quantity
