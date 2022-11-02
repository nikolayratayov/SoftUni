from project.food.food import Food


class Starter(Food):
    def __init__(self, name, price, grams):
        super(Starter, self).__init__(name, price, grams)
