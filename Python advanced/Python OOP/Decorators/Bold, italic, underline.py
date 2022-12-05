def make_bold(function):
    def dec(*args):
        return f'<b>{function(*args)}</b>'
    return dec


def make_italic(function):
    def dec(*args):
        return f'<i>{function(*args)}</i>'
    return dec


def make_underline(function):
    def dec(*args):
        return f'<u>{function(*args)}</u>'
    return dec
