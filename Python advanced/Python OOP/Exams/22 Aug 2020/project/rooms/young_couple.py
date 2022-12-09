from project.rooms.room import Room


class YoungCouple(Room):

    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, 2, 7.4 * 30)
        self.room_cost = 20