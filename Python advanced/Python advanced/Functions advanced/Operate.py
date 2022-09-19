def operate(sign, *args):
    if sign == '+':
        return sum(args)
    elif sign == '-':
        res = args[0]
        for i in range(1, len(args)):
            res -= args[i]
        return res
    elif sign == '*':
        res = 1
        for i in args:
            res *= i
        return res
    elif sign == '/':
        res = args[0]
        for i in range(1, len(args)):
            res /= args[i]
        return res
