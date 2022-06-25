people = int(input())
lift_str = input().split(' ')
lift = [int(x) for x in lift_str]
no_more_space_on_lift = False
while True:
    if people == 0 or no_more_space_on_lift:
        break
    index = -1
    for i in lift:
        index += 1
        if i < 4:
            lift[index] += 1
            people -= 1
            break
    no_more_space_on_lift = True
    for i in lift:
        if i != 4:
            no_more_space_on_lift = False
lift_final_str = [str(x) for x in lift]
if people == 0 and no_more_space_on_lift:
    print(' '.join(lift_final_str))
elif people == 0 and not no_more_space_on_lift:
    print('The lift has empty spots!')
    print(' '.join(lift_final_str))
else:
    print(f'There isn\'t enough space! {people} people in a queue!')
    print(' '.join(lift_final_str))
