from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos):
        if race_pos == 1:
            revenue = 900000
        elif race_pos <= 3:
            revenue = 400000
        elif race_pos <= 5:
            revenue = -100000
        elif race_pos <= 7:
            revenue = -150000
        else:
            revenue = -200000
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
