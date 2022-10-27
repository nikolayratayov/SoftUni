class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new):
        if new == self.name:
            return "Name cannot be the same."
        self.name = new
        return new

    def change_due_date(self, new):
        if self.due_date == new:
            return "Date cannot be the same."
        self.due_date = new
        return new

    def add_comment(self, com):
        self.comments.append(com)

    def edit_comment(self, num, new):
        if num < 0 or num >= len(self.comments):
            return "Cannot find comment."
        self.comments[num] = new
        return ', '.join(self.comments)

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
