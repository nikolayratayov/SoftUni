class Inventory:
    def __init__(self, __capacity):
        self.__capacity = __capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.__capacity:
            self.items.append(item)

        else:
            a = 'not enough room in the inventory'
            return a

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        a = f'Items: {", ".join(self.items)}.\nCapacity left: {self.__capacity - len(self.items)}'
        return a
