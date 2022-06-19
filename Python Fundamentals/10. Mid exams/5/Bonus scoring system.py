import math


students = int(input())
lectures = int(input())
bonus = int(input())
student_points = []
total_attendances = []
for i in range(students):
    attendances = int(input())
    total_attendances.append(attendances)
    total_bonus = math.ceil(attendances / lectures * (5 + bonus))
    student_points.append(total_bonus)
if students == 0:
    print('Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
else:
    print(f'Max Bonus: {max(student_points)}.')
    get_index = student_points.index(max(student_points))
    print(f'The student has attended {total_attendances[get_index]} lectures.')
