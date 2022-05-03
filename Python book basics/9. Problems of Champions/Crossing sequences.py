a = int(input())
b = int(input())
c = int(input())
nach = int(input())
step = int(input())
# do 1 milion
x = 0
trib = [a, b, c]
ima = False
while True:
    olda = a
    oldb = b
    oldc = c
    x = olda + oldb + oldc
    a = b
    b = c
    c = x
    if x <= 1000000:
        trib.append(x)
    else:
        break
for i in range(1, 200):
    if nach in trib:
        print(nach)
        ima = True
        break
    nach += i * step
    if nach in trib:
        print(nach)
        ima = True
        break
    nach += i * step
    if nach in trib:
        print(nach)
        ima = True
        break
if not ima:
    print('No')
