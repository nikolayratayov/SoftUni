from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget):
        if budget < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.budget = int(budget)

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos):
        pass
