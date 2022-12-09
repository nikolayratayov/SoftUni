from project.rooms.room import Room


class AloneYoung(Room):

    def __init__(self, family_name, salary):
        super().__init__(family_name, salary, 1, 1.5 * 30)
        self.room_cost = 10
