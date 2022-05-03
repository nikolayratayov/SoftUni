n = int(input())
kolona = n // 2
mid = 2 * n - 2 * kolona - 4
print('/{0}\\{1}/{0}\\'.format('^' * kolona, '_' * mid))
for row in range(n - 3):
    print('|{0}|'.format(' ' * (2 * n - 2)))
print('|{0}{1}{0}|'.format(' ' * (kolona + 1), '_' * mid))
print('\\{0}/{1}\\{0}/'.format('_' * kolona, ' ' * mid))
