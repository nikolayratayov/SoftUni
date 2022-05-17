class Circle:
    __pi = 3.14

    def __init__(self, diam):
        self.diam = diam

    def calculate_circumference(self):
        return Circle.__pi * self.diam

    def calculate_area(self):
        return Circle.__pi * self.diam ** 2 / 4

    def calculate_area_of_sector(self, angle):
        return Circle.calculate_area(self) * angle / 360

