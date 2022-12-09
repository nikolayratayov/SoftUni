from project.software.software import Software


class ExpressSoftware(Software):

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, 'Express', capacity_consumption, 2 * memory_consumption)
