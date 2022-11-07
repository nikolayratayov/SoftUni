class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        res = 1
        for i in args:
            res *= i
        return res

    @staticmethod
    def divide(*args):
        num = args[0]
        for i in range(1, len(args)):
            num /= args[i]
        return num

    @staticmethod
    def subtract(*args):
        num = args[0]
        for i in range(1, len(args)):
            num -= args[i]
        return num
