class Hardware:

    def __init__(self, name, hardware_type, capacity, memory):
        self.name = str(name)
        self.hardware_type = str(hardware_type)
        self.capacity = int(capacity)
        self.memory = int(memory)
        self.software_components = []
        self.memory_taken = 0
        self.capacity_taken = 0

    def install(self, software):
        if software.memory_consumption <= (self.memory - self.memory_taken) and software.capacity_consumption <= (self.capacity - self.capacity_taken):
            self.software_components.append(software)
            self.memory_taken += software.memory_consumption
            self.capacity_taken += software.capacity_consumption
        else:
            raise Exception('Software cannot be installed')

    def uninstall(self, software):
        self.software_components.remove(software)
        self.memory_taken -= software.memory_consumption
        self.capacity_taken -= software.capacity_consumption
