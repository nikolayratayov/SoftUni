# def get_fibonacci(n):
#     if n == 1 or n == 0:
#         return 1
#     return get_fibonacci(n - 1) + get_fibonacci(n - 2)
#
#
# n = int(input())
# print(get_fibonacci(n))


n = int(input())
num1 = 1
num2 = 1
result = 0
for i in range(n - 1):
    result = num1 + num2
    num1 = num2
    num2 = result
print(result)