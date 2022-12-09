from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCoupleWithChildren(Room):

    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.room_cost = 30
        self.children = children
        temp_lst = []
        for i in range(len(children) + 2):
            temp_lst.append(TV())
            temp_lst.append(Fridge())
            temp_lst.append(Laptop())
        temp_lst += children
        self.calculate_expense(temp_lst)

