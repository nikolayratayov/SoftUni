def recursive_power(num, power):

    if power == 1:
        return num
    elif power == 0:
        return 1
    return recursive_power(num, power - 1) * num
