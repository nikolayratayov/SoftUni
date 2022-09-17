import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    email = input()
    if email == 'End':
        break

    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    regex_name = r'^(\w+)@'
    name = re.findall(regex_name, email)
    if len(name[0]) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    regex_domain = r'\.com$|\.org$|\.bg$|\.net$'
    domain = re.search(regex_domain, email)
    if not domain:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')
