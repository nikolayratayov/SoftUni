class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        res = f'Name: {self.name}\n'
        res += f'Guild: {self.guild}\n'
        res += f'HP: {self.hp}\n'
        res += f'MP: {self.mp}\n'
        for k, v in self.skills.items():
            res += f'==={k} - {v}\n'
        return res[0:len(res) - 1]
