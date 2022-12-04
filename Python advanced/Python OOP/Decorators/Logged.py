def logged(func):
    def decorator(*args):
        return f'you called {func.__name__}({", ".join(str(x) for x in args)})\nit returned {func(*args)}'
    return decorator
