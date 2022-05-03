l = float(input())
w = float(input())
while not int(w) in range(3, 100):
    w = float(input())
while not int(l) in range(3, 100):
    l = float(input())
while not l >= w:
    l = float(input())
row = ((w*100)-100) // 70
column = (l*100) // 120
result = row*column-3
print(int(result))