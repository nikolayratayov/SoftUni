import re


n = int(input())
for _ in range(n):
    barcode = input()
    regex = r'@[#]+[A-Z][A-Za-z0-9]{4}[A-Za-z0-9]*[A-Z]@[#]+'
    try:
        search = re.search(regex, barcode).group()
        digits = ''
        for i in search:
            if i.isdigit():
                digits += i
        if len(digits) == 0:
            print('Product group: 00')
        else:
            print(f'Product group: {digits}')
    except:
        print('Invalid barcode')
