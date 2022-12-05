def even_parameters(function):
    def dec(*args):
        for i in args:
            if not isinstance(i, int) or i % 2 != 0:
                return 'Please use only even numbers!'
        return function(*args)
    return dec
