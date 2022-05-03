def nthd(number, index):
    a = len(number)
    b = a - index
    c = number[b]
    print(c)


number = input()
index = int(input())
nthd(number, index)
