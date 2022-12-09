from project.rooms.room import Room


class OldCouple(Room):

    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two, 2, 6.8 * 30)
        self.room_cost = 15
