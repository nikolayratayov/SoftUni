def tags(tag):
    def dec(func):
        def wrapper(*args):
            return f'<{tag}>{func(*args)}</{tag}>'
        return wrapper
    return dec
