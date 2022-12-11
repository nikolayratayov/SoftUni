class Client:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        offf = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in value:
            if i not in offf:
                raise ValueError("Invalid phone number!")
        if value[0] != '0' or len(value) != 10:
            raise ValueError("Invalid phone number!")
        self.__phone_number = value
