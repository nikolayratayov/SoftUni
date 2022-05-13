a = int(input())
b = int(input())
print('Before:')
print(f'a = {a}')
print(f'b = {b}')
b_vr = a
a_vr = b
b = b_vr
a = a_vr
print('After:')
print(f'a = {a}')
print(f'b = {b}')