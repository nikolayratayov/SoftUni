izpit_h = int(input())
izpit_m = int(input())
student_h = int(input())
student_m = int(input())
late = "Late"
on_time = 'On time'
early = 'Early'
izpit_time = izpit_h * 60 + izpit_m
student_time = student_h * 60 + student_m
if (izpit_time == student_time) or ((izpit_time - 30) <= student_time <= izpit_time):
    if izpit_time == student_time:
        print(on_time)
    elif (izpit_time - 30) <= student_time <= izpit_time:
        razlika_m = izpit_time - student_time
        print(on_time+f' {razlika_m} minutes before the start')
elif student_time < (izpit_time - 30):
    razlika_m = izpit_time - student_time
    if razlika_m >= 60:
        razlika_h = razlika_m // 60
        razlika_m = razlika_m % 60
        if razlika_m < 10:
            print(early+f' {razlika_h}:0{razlika_m} hours before the start')
        else:
            print(early + f' {razlika_h}:{razlika_m} hours before the start')
    else:
        print(early+f' {razlika_m} minutes before the start')
else:
    razlika_m = student_time - izpit_time
    if razlika_m >= 60:
        razlika_h = razlika_m // 60
        razlika_m = razlika_m % 60
        if razlika_m < 10:
            print(late+f' {razlika_h}:0{razlika_m} hours after the start')
        else:
            print(late + f' {razlika_h}:{razlika_m} hours after the start')
    else:
        print(late+f' {razlika_m} minutes after the start')
