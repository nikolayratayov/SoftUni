class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, prod):
        self.products.append(prod)

    def find(self, product_name):
        for i in self.products:
            if i.name == product_name:
                return i

    def remove(self, product_name):
        for i in self.products:
            if i.name == product_name:
                self.products.remove(i)

    def __repr__(self):
        res = ''
        for i in self.products:
            res += i.name + ': ' + str(i.quantity) + '\n'
        return res[0: len(res) - 1]
