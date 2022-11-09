from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos):
        if race_pos == 1:
            revenue = 1270000
        elif race_pos == 2:
            revenue = 570000
        elif race_pos <= 8:
            revenue = -230000
        elif race_pos <= 10:
            revenue = -240000
        else:
            revenue = -250000
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"