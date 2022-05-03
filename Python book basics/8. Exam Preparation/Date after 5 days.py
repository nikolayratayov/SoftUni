import datetime
m = int(input())
d = int(input())
x = datetime.date(2022, d, m)
z = x + datetime.timedelta(days=5)
mesec = z.strftime('%m')
den = z.strftime('%d').lstrip('0')
print(f'{den}.{mesec}')
