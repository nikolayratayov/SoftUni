def rec_fac(a):
    if a == 1:
        return 1
    return a * rec_fac(a - 1)


a = int(input())
print(rec_fac(a))