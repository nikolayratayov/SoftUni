from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type, horse_name, horse_speed):
        for i in self.horses:
            if i.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type == 'Appaloosa':
            self.horses.append(Appaloosa(horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."
        elif horse_type == 'Thoroughbred':
            self.horses.append(Thoroughbred(horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        for i in self.jockeys:
            if i.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        for i in self.horse_races:
            if i.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                for idx_horse in range(len(self.horses) - 1, -1, -1):
                    if self.horses[idx_horse].__class__.__name__ == horse_type and not self.horses[idx_horse].is_taken:
                        if jockey.horse:
                            return f"Jockey {jockey_name} already has a horse."
                        else:
                            self.horses[idx_horse].is_taken = True
                            jockey.horse = self.horses[idx_horse]
                            return f"Jockey {jockey_name} will ride the horse {self.horses[idx_horse].name}."
                raise Exception(f"Horse breed {horse_type} could not be found!")
        raise Exception(f"Jockey {jockey_name} could not be found!")

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        for race in self.horse_races:
            if race.race_type == race_type:
                for jockey in self.jockeys:
                    if jockey.name == jockey_name:
                        if jockey.horse:
                            if jockey in race.jockeys:
                                return f"Jockey {jockey_name} has been already added to the {race_type} race."
                            else:
                                race.jockeys.append(jockey)
                                return f"Jockey {jockey_name} added to the {race_type} race."
                        else:
                            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
                raise Exception(f"Jockey {jockey_name} could not be found!")
        raise Exception(f"Race {race_type} could not be found!")

    def start_horse_race(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                if len(race.jockeys) > 1:
                    res = sorted(race.jockeys, key=lambda x: x.horse.speed, reverse=True)
                    return f"The winner of the {race_type} race, with a speed of {res[0].horse.speed}km/h is {res[0].name}! Winner's horse: {res[0].horse.name}."
                else:
                    raise Exception(f"Horse race {race_type} needs at least two participants!")
        raise Exception(f"Race {race_type} could not be found!")


# horseRaceApp = HorseRaceApp()
# print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
# print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
# print(horseRaceApp.add_jockey("Peter", 19))
# print(horseRaceApp.add_jockey("Mariya", 21))
# print(horseRaceApp.create_horse_race("Summer"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
# print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.start_horse_race("Summer"))
