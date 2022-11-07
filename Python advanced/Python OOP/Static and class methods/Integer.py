def eee(r):
    if r == 'I':
        return 1
    if r == 'V':
        return 5
    if r == 'X':
        return 10
    if r == 'L':
        return 50
    if r == 'C':
        return 100
    if r == 'D':
        return 500
    if r == 'M':
        return 1000
    return -1


def romanToDecimal(input_Str):
    res = 0
    i = 0
    while (i < len(input_Str)):

        s1 = eee(input_Str[i])
        if (i + 1 < len(input_Str)):
            s2 = eee(input_Str[i + 1])
            if (s1 >= s2):
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    return res


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return 'value is not a float'
        else:
            return cls(int(value))

    @classmethod
    def from_roman(cls, value):
        return cls(romanToDecimal(value))

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return 'wrong type'
        try:
            value = int(value)
            return cls(value)
        except:
            return 'wrong type'
