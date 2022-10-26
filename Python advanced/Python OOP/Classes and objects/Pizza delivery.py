class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, price):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity
        self.price += price * quantity

    def remove_ingredient(self, ingredient, quantity, price):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
        else:
            if quantity > self.ingredients[ingredient]:
                return f'Please check again the desired quantity of {ingredient}!'
        self.ingredients[ingredient] -= quantity
        self.price -= price * quantity

    def make_order(self):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        self.ordered = True
        lst = [f'{k}: {v}' for k, v in self.ingredients.items()]
        return f'You\'ve ordered pizza {self.name} prepared with {", ".join(lst)} and the price will be {self.price}lv.'
