seats = [x for x in input().split(', ')]
se1 = [int(x) for x in input().split(', ')]
se2 = [int(x) for x in input().split(', ')]
rotations = 0
seat_matches = []

while True:
    if len(seat_matches) == 3:
        break
    if rotations == 10:
        break
    rotations += 1
    first = se1[0]
    second = se2[-1]
    letter = chr(first + second)
    seat = str(first) + letter
    if seat in seats:
        se1.pop(0)
        se2.pop()
        if seat not in seat_matches:
            seat_matches.append(seat)
        continue
    seat = str(second) + letter
    if seat in seats:
        se1.pop(0)
        se2.pop()
        if seat not in seat_matches:
            seat_matches.append(seat)
        continue
    se1.append(se1.pop(0))
    se2.insert(0, se2.pop())
print(f'Seat matches: {", ".join(seat_matches)}')
print(f'Rotations count: {rotations}')
