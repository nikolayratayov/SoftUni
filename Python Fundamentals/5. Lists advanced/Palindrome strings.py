lst = input().split(' ')
a = input()
vs_pl = [i for i in lst if i == i[::-1]]
count = 0
for i in vs_pl:
    if i == a:
        count += 1
print(vs_pl)
print(f'Found palindrome {count} times')
