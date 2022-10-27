class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new):
        if new in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new)
        return f"Task {new.details()} is added to the section"

    def complete_task(self, name):
        for i in self.tasks:
            if i.name == name:
                i.completed = True
                return f"Completed task {name}"
        return f"Could not find task with the name {name}"

    def clean_section(self):
        counter = 0
        for i in range(len(self.tasks) - 1, -1, -1):
            if self.tasks[i].completed:
                self.tasks.pop(i)
                counter += 1
        return f"Cleared {counter} tasks."

    def view_section(self):
        res = f"Section {self.name}:\n"
        for i in self.tasks:
            res += f'{i.details()}\n'
        return res[0:len(res) - 1]
