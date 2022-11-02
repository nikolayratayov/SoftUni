class Dough:
    def __init__(self, flour_type, baking_technique, weight):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, new):
        if not new:
            raise ValueError("The flour type cannot be an empty string")
        self.__flour_type = new

    @property
    def baking_technique(self):
        return self.__baking_technique

    @baking_technique.setter
    def baking_technique(self, new):
        if not new:
            raise ValueError("The baking technique cannot be an empty string")
        self.__baking_technique = new

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new):
        if new <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = new
