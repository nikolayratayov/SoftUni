from project.animals.animal import Bird


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return 'Hoot Hoot'

    def feed(self, food):
        if food.__class__.__name__ != 'Meat':
            return f"Owl does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.25
        self.food_eaten += food.quantity


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return 'Cluck'

    def feed(self, food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity
