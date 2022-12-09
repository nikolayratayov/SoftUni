class Room:

    def __init__(self, family_name, budget, members_count, expenses=0):
        if expenses < 0:
            raise ValueError('Expenses cannot be negative')
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = expenses

    def calculate_expense(self, args):
        exp = 0
        for i in args:
            if i.__class__.__name__ == 'Child':
                exp += i.cost * 30
            else:
                exp += i.get_monthly_expense()
        self.expenses = exp
