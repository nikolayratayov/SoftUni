from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name, budget):
        if team_name == 'Red Bull':
            self.red_bull_team = RedBullTeam(budget)
            return f"{team_name} has joined the new F1 season."
        elif team_name == 'Mercedes':
            self.mercedes_team = MercedesTeam(budget)
            return f"{team_name} has joined the new F1 season."
        else:
            raise ValueError("Invalid team name!")

    def new_race_results(self, race_name, red_bull_pos, mercedes_pos):
        if self.mercedes_team is None or self.red_bull_team is None:
            raise Exception("Not all teams have registered for the season.")
        else:
            red_bull_message = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
            mercedes_message = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)
            if red_bull_pos < mercedes_pos:
                better_team = 'Red Bull'
            else:
                better_team = 'Mercedes'
            return f"Red Bull: {red_bull_message}. Mercedes: {mercedes_message}. {better_team} is ahead at the {race_name} race."
