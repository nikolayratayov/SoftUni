a = input().split('\\')
b = a[-1].split('.')
name = b[0]
ext = b[1]
print(f'File name: {name}')
print(f'File extension: {ext}')
