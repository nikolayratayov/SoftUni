class Class:
    __student_count = 0

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if self.__student_count < 22:
            self.students.append(name)
            self.grades.append(grade)
            self.__student_count += 1

    def get_average_grade(self):
        a = f'{(sum(self.grades) / len(self.grades)):.2f}'
        b = float(a)
        return b

    def __repr__(self):
        a = f'The students in {self.name}: {", ".join(self.students)}. Average grade: {self.get_average_grade()}'
        return a
