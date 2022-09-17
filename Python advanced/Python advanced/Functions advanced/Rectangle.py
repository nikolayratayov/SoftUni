def rectangle(length, width):

    def area(a, b):
        return a * b

    def perimeter(a, b):
        return 2 * a + 2 * b

    if type(length) == int and type(width) == int:
        return f'Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}'
    else:
        return 'Enter valid values!'
