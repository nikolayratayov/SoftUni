class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        for i in self.customers:
            if i.id == customer_id:
                for j in i.rented_dvds:
                    if j.id == dvd_id:
                        return f"{i.name} has already rented {j.name}"

        for i in self.dvds:
            if i.id == dvd_id:
                if i.is_rented:
                    return "DVD is already rented"

        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd.age_restriction > customer.age:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                        else:
                            customer.rented_dvds.append(dvd)
                            dvd.is_rented = True
                            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = False
                        customer.rented_dvds.remove(dvd)
                        return f'{customer.name} has successfully returned {dvd.name}'
        for customer in self.customers:
            if customer.id == customer_id:
                return f"{customer.name} does not have that DVD"

    def __repr__(self):
        res = ''
        for i in self.customers:
            res += repr(i) + '\n'
        for i in self.dvds:
            res += repr(i) + '\n'
        return res[0: len(res) - 1]
