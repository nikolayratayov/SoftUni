class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        res = ''
        for i in self.subscriptions:
            if i.id == subscription_id:
                res += repr(i) + '\n'
                customer_id = i.customer_id
                trainer_id = i.trainer_id
                exercise_id = i.exercise_id
                break

        for i in self.customers:
            if i.id == customer_id:
                res += repr(i) + '\n'
                break

        for i in self.trainers:
            if i.id == trainer_id:
                res += repr(i) + '\n'

        for i in self.plans:
            if i.id == exercise_id:
                equipment_id = i.equipment_id
                for j in self.equipment:
                    if j.id == equipment_id:
                        res += repr(j) + '\n'
                res += repr(i)

        return res
