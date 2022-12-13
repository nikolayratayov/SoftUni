from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        types = ['Gingerbread', 'Stolen']
        for i in self.delicacies:
            if i.name == name:
                raise Exception(f"{name} already exists!")
        if type_delicacy not in types:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        if type_delicacy == 'Gingerbread':
            self.delicacies.append(Gingerbread(name, price))
        elif type_delicacy == 'Stolen':
            self.delicacies.append(Stolen(name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        valid = ['Open Booth', 'Private Booth']
        for i in self.booths:
            if i.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in valid:
            raise Exception(f"{type_booth} is not a valid booth!")
        if type_booth == 'Open Booth':
            self.booths.append(OpenBooth(booth_number, capacity))
        elif type_booth == 'Private Booth':
            self.booths.append(PrivateBooth(booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = None
        delicacy = None
        for i in self.booths:
            if i.booth_number == booth_number:
                booth = i
        for i in self.delicacies:
            if i.name == delicacy_name:
                delicacy = i
        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")
        if delicacy is None:
            raise Exception(f'No {delicacy_name} in the pastry shop!')
        booth.delicacy_order.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                bill = booth.price_for_reservation
                for i in booth.delicacy_order:
                    bill += i.price
                self.income += bill
                booth.delicacy_order = []
                booth.is_reserved = False
                booth.price_for_reservation = 0
                # return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."



shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].name)
print(shop.add_delicacy('Stolen', 'das', 15.5))
print(shop.delicacies[1].name)
print(shop.add_delicacy('Gingerbread', 'gfdg', 1213.5165))
print(shop.delicacies[2].name)

print(shop.add_booth('Private Booth', 10, 10))
print(shop.add_booth('Private Booth', 1, 1))
print(shop.add_booth('Private Booth', 2, 2))
print(shop.add_booth('Open Booth', 3, 3))
print(shop.reserve_booth(2))
print(shop.reserve_booth(2))
print(shop.booths[0].is_reserved)
print(shop.booths[1].is_reserved)

print(shop.order_delicacy(10, 'das'))
print(shop.leave_booth(10))

print(shop.reserve_booth(10))
print(shop.order_delicacy(10, 'das'))
print(shop.leave_booth(10))