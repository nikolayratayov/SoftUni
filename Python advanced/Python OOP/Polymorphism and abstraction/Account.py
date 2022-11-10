class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        if self.amount + sum(self._transactions) + transaction_amount < 0:
            raise ValueError('sorry cannot go in debt!')
        else:
            self._transactions.append(transaction_amount)
            return f"New balance: {self.amount + sum(self._transactions)}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        else:
            self.handle_transaction(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        for i in self._transactions:
            yield i

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        new = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        for i in self:
            new.add_transaction(i)
        for i in other:
            new.add_transaction(i)
        return new

    def __getitem__(self, item):
        return self._transactions[item]
