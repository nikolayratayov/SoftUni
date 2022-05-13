n = int(input())
stara = 0
for i in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if value > stara:
        zapw = weight
        zapt = time
        zapq = quality
        stara = value

print(f'{zapw} : {zapt} = {int(stara)} ({zapq})')
