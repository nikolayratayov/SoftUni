class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new):
        if not new:
            raise ValueError("The name cannot be an empty string")
        self.__name = new

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, new):
        if new is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = new

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, new):
        if new <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = new

    def add_topping(self, top):
        if self.toppings_capacity == len(self.toppings):
            raise ValueError("Not enough space for another topping")
        if top.topping_type in self.toppings:
            self.toppings[top.topping_type] += top.weight
        else:
            self.toppings[top.topping_type] = top.weight

    def calculate_total_weight(self):
        total = self.dough.weight
        for k, v in self.toppings.items():
            total += v
        return total
