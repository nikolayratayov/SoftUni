import re


n = input().split(' ')
while True:
    a = input()
    if a == 'find':
        break
    b = ''
    ind_key = -1
    for i in range(0, len(a)):
        ind_key += 1
        if ind_key == len(n):
            ind_key = 0
        b += chr(ord(a[i]) - int(n[ind_key]))
        if i == len(a) - 1:
            treasure = re.search('&.*&', b).group()
            treasure = treasure.replace('&', '')
            coordinates = re.search('<.*>', b).group()
            coordinates = coordinates.replace('<', '')
            coordinates = coordinates.replace('>', '')
            print(f'Found {treasure} at {coordinates}')
