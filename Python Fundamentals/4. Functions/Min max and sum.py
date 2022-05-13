a = input().split(' ')
b = []
for i in a:
    b.append(int(i))

print(f'The minimum number is {min(b)}')
print(f'The maximum number is {max(b)}')
print(f'The sum number is: {sum(b)}')
