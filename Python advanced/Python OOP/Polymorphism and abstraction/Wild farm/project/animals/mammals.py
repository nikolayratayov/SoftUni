from project.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return 'Squeak'

    def feed(self, food):
        if food.__class__.__name__ != 'Vegetable' and food.__class__.__name__ != 'Fruit':
            return f"Mouse does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.1
        self.food_eaten += food.quantity


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return 'Woof!'

    def feed(self, food):
        if food.__class__.__name__ != 'Meat':
            return f"Dog does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.4
        self.food_eaten += food.quantity


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return 'Meow'

    def feed(self, food):
        if food.__class__.__name__ != 'Meat' and food.__class__.__name__ != 'Vegetable':
            return f"Cat does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.3
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return 'ROAR!!!'

    def feed(self, food):
        if food.__class__.__name__ != 'Meat':
            return f"Tiger does not eat {food.__class__.__name__}!"
        self.weight += food.quantity
        self.food_eaten += food.quantity
