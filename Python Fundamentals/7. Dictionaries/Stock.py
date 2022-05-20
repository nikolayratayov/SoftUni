a = input().split(' ')
products = {}
for i in range(0, len(a), 2):
    products[a[i]]=int(a[i + 1])

b = input().split()
for i in b:
    if i in products:
        print(f'We have {products[i]} of {i} left')
    else:
        print(f'Sorry, we don\'t have {i}')
