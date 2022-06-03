start = input()
end = input()
seq = input()
lst = []
for i in seq:
    if ord(start) < ord(i) < ord(end):
        lst.append(ord(i))
print(sum(lst))
