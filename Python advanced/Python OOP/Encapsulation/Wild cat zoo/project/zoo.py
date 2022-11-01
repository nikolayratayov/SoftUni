class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > 0 and price > self.__budget:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        for i in self.workers:
            if i.name == worker_name:
                self.workers.remove(i)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = 0
        for i in self.workers:
            sum_salaries += i.salary
        if sum_salaries <= self.__budget:
            self.__budget -= sum_salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_care = 0
        for i in self.animals:
            sum_care += i.money_for_care
        if sum_care <= self.__budget:
            self.__budget -= sum_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        res = f'You have {len(self.animals)} animals\n'
        list_of_lions = []
        list_of_tigers = []
        list_of_cheetahs = []
        for i in self.animals:
            if i.__class__.__name__ == 'Lion':
                list_of_lions.append(i)
            elif i.__class__.__name__ == 'Tiger':
                list_of_tigers.append(i)
            else:
                list_of_cheetahs.append(i)
        res += f'----- {len(list_of_lions)} Lions:\n'
        for i in list_of_lions:
            res += f'{repr(i)}\n'
        res += f'----- {len(list_of_tigers)} Tigers:\n'
        for i in list_of_tigers:
            res += f'{repr(i)}\n'
        res += f'----- {len(list_of_cheetahs)} Cheetahs:\n'
        for i in list_of_cheetahs:
            res += f'{repr(i)}\n'
        return res[0:len(res) - 1]

    def workers_status(self):
        res = f"You have {len(self.workers)} workers\n"
        list_of_keepers = []
        list_of_caretakers = []
        list_of_vets = []
        for i in self.workers:
            if i.__class__.__name__ == 'Keeper':
                list_of_keepers.append(i)
            elif i.__class__.__name__ == 'Vet':
                list_of_vets.append(i)
            else:
                list_of_caretakers.append(i)
        res += f'----- {len(list_of_keepers)} Keepers:\n'
        for i in list_of_keepers:
            res += f'{repr(i)}\n'
        res += f'----- {len(list_of_caretakers)} Caretakers:\n'
        for i in list_of_caretakers:
            res += f'{repr(i)}\n'
        res += f'----- {len(list_of_vets)} Vets:\n'
        for i in list_of_vets:
            res += f'{repr(i)}\n'
        return res[0:len(res) - 1]

