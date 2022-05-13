def perfect(num):
    lst = []
    for i in range(1, num):
        if num % i == 0:
            lst.append(i)
    if sum(lst) == num:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')


a = int(input())
perfect(a)
