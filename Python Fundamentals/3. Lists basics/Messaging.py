numbers = input().split(' ')
neshtosiii = input()
neshtosi = []
for i in neshtosiii:
    neshtosi.append(i)
nov = []
for i in numbers:
    a = []
    for j in i:
        a.append(int(j))
    nov.append(sum(a))

message = ''
for i in nov:
    if i >= len(neshtosi):
        index = i // len(neshtosi)
        message += neshtosi[index]
        neshtosi.pop(index)
        continue
    index = i
    message += neshtosi[index]
    neshtosi.pop(index)

print(message)
