def multiply(a, b):
    return int(a * b)


def divide(a, b):
    return int(a / b)


def add(a, b):
    return int(a + b)


def subtract(a, b):
    return int(a - b)


neshto = input()
a = int(input())
b = int(input())

if neshto == 'multiply':
    print(multiply(a, b))
elif neshto == 'divide':
    print(divide(a, b))
elif neshto == 'subtract':
    print(subtract(a, b))
elif neshto == 'add':
    print(add(a, b))
