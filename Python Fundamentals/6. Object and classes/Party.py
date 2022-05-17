class Party:
    def __init__(self):
        self.people = []


party = Party()

while True:
    a = input()
    if a == 'End':
        break
    party.people.append(a)

print(f'Going: {", ".join(party.people)}')
print(f'Total: {len(party.people)}')