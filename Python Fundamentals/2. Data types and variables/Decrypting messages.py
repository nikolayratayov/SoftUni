key = int(input())
n = int(input())
izraz = ''
for i in range(n):
    bukva = input()
    decrypted = chr(ord(bukva) + key)
    izraz += decrypted

print(izraz)