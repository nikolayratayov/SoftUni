def get_expr(start, end):
    expressions.append(string[start: end + 1])


string = input()
stack = []
expressions = []
for i in range(0, len(string)):
    if string[i] == '(':
        stack.append(i)
    if string[i] == ')':
        get_expr(stack.pop(), i)

print('\n'.join(expressions))
