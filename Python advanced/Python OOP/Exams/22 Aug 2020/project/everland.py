import copy
# from rooms.young_couple import YoungCouple
# from rooms.young_couple_with_children import YoungCoupleWithChildren
# from people.child import Child




class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        res = 0
        for i in self.rooms:
            res += i.expenses
            res += i.room_cost
        return f'Monthly consumption: {res:.2f}$.'

    def pay(self):
        res = ''
        temp_rooms = copy.copy(self.rooms)
        for i in temp_rooms:
            if i.budget >= i.expenses + i.room_cost:
                i.budget -= i.expenses + i.room_cost
                res += f'"{i.family_name} paid {(i.expenses + i.room_cost):.2f}$ and have {(i.budget):.2f}$ left.\n'
            else:
                res += f'{i.family_name} does not have enough budget and must leave the hotel.\n'
                self.rooms.remove(i)
        return res

    def status(self):
        res = ''
        total_population = 0
        for i in self.rooms:
            total_population += i.members_count
        res += f'Total population: {total_population}\n'
        for i in self.rooms:
            res += f'{i.family_name} with {i.members_count} members. Budget: {i.budget:.2f}$, Expenses: {i.expenses:.2f}$\n'
            children_costs = 0
            if len(i.children) > 0:
                count_child = 0
                for child in i.children:
                    count_child += 1
                    res += f'--- Child {count_child} monthly cost: {(child.cost * 30):.2f}$\n'
                    children_costs += child.cost * 30
            res += f'--- Appliances monthly cost: {(i.expenses - children_costs):.2f}$\n'
        return res


# everland = Everland()
#
#
# def test_one():
#     young_couple = YoungCouple("Johnsons", 150, 205)
#
#     child1 = Child(5, 1, 2, 1)
#     child2 = Child(3, 2)
#     young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
#
#     everland.add_room(young_couple)
#     everland.add_room(young_couple_with_children)
#
#     print(everland.get_monthly_consumptions())
#     print(everland.pay())
#     print(everland.status())
#
#
#
# test_one()
