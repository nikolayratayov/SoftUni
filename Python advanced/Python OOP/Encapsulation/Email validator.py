import re


class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        if len(name) >= self.min_length:
            return True
        return False

    def __is_mail_valid(self, mail):
        if mail in self.mails:
            return True
        return False

    def __is_domain_valid(self, domain):
        if domain in self.domains:
            return True
        return False

    def validate(self, email):
        regex_name = r'(\A[A-Za-z]+)@'
        name = re.search(regex_name, email).group(1)

        regex_mail = r'@([a-zA-z0-9]+)\.'
        mail = re.search(regex_mail, email).group(1)

        regex_domain = r'\.([a-zA-Z0-9]+\Z)'
        domain = re.search(regex_domain, email).group(1)

        return EmailValidator.__is_name_valid(self, name) and EmailValidator.__is_mail_valid(self, mail) and EmailValidator.__is_domain_valid(self, domain)

