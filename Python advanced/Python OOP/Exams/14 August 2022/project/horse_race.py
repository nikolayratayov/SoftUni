class HorseRace:
    def __init__(self, race_type):
        self.race_type = race_type
        self.jockeys = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        a = ['Winter', 'Spring', 'Autumn', 'Summer']
        if value not in a:
            raise ValueError('Race type does not exist!')
        self.__race_type = value
