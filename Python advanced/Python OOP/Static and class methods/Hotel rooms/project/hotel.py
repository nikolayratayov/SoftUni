class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        self.guests += people
        for i in self.rooms:
            if room_number == i.number:
                i.take_room(people)

    def free_room(self, room_number):
        for i in self.rooms:
            if room_number == i.number:
                self.guests -= i.guests
                i.free_room()

    def status(self):
        res = f'Hotel {self.name} has {self.guests} total guests\n'
        free_rooms = []
        taken_rooms = []
        for i in self.rooms:
            if not i.is_taken:
                free_rooms.append(i.number)
            else:
                taken_rooms.append(i.number)
        res += f'Free rooms: {", ".join(str(x) for x in free_rooms)}\n'
        res += f'Taken rooms: {", ".join(str(x) for x in taken_rooms)}'
        return res
