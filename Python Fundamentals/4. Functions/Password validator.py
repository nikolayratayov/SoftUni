def valid_pass(a):
    valid_len = False
    valid_dig = True
    two_dig = False
    digits = 0
    if 6 <= len(a) <= 10:
        valid_len = True
    for i in a:
        if not 48 <= ord(i) <= 57 and not 65 <= ord(i) <= 90 and not 97 <= ord(i) <= 122:
            valid_dig = False
        if 48 <= ord(i) <= 57:
            digits += 1

    if digits >= 2:
        two_dig = True

    if not valid_len:
        print('Password must be between 6 and 10 characters')
    if not valid_dig:
        print('Password must consist only of letters and digits')
    if not two_dig:
        print('Password must have at least 2 digits')
    if valid_dig and valid_len and two_dig:
        print('Password is valid')


a = input()
valid_pass(a)
