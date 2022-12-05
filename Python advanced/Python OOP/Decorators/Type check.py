def type_check(t):
    def dec(func):
        def wrapper(argument):
            if isinstance(argument, t):
                return func(argument)
            return 'Bad Type'
        return wrapper
    return dec
