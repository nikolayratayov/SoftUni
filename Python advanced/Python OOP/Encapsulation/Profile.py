import re


class Profile:
    def __init__(self, username, password):
        if len(username) < 5 or len(username) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        else:
            self.username = username
        if re.search(r'\d', password) and re.search(r'[A-Z]', password) and len(password) > 7:
            self.password = password
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
