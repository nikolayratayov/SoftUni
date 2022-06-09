participants = input().split(', ')
participants_dict = {}
while True:
    a = input()
    if a == 'end of race':
        break
    number = 0
    name = ''
    for i in a:
        if ord(i) in range(48, 58):
            number += int(i)
        elif ord(i) in range(65, 91) or ord(i) in range(97, 123):
            name += i
    if name in participants:
        if name not in participants_dict:
            participants_dict[name] = number
        else:
            temp = participants_dict[name]
            participants_dict[name] = temp + number
sorted_dict = {k: v for k, v in sorted(participants_dict.items(), key=lambda item: item[1], reverse=True)}
count = 0
for i in sorted_dict:
    count += 1
    if count == 1:
        print(f'1st place: {i}')
    elif count == 2:
        print(f'2nd place: {i}')
    elif count == 3:
        print(f'3rd place: {i}')
