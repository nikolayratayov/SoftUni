class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, letter):
        lst = [i for i in self.products if i.startswith(letter)]
        return lst

    def __repr__(self):
        self.products.sort()
        eeee = '\n'.join(self.products)
        a = f'Items in the {self.name} catalogue:\n' \
                f'{eeee}'
        return a


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

