class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        else:
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            return print(f'Mammals in {self.name}: {", ".join(self.mammals)}\nTotal animals: {Zoo.__animals}')
        elif species == 'fish':
            return print(f'Fishes in {self.name}: {", ".join(self.fishes)}\nTotal animals: {Zoo.__animals}')
        else:
            return print(f'Birds in {self.name}: {", ".join(self.birds)}\nTotal animals: {Zoo.__animals}')


zooooooo = Zoo(input())
n = int(input())
for i in range(n):
    a = input().split(' ')
    zooooooo.add_animal(a[0], a[1])

a = input()
zooooooo.get_info(a)
