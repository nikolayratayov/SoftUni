def vowel_filter(function):
    def wrapper():
        res = function()
        return [x for x in res if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u']
    return wrapper
