from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, cap, mem):
        System._hardware.append(PowerHardware(name, cap, mem))

    @staticmethod
    def register_heavy_hardware(name, cap, mem):
        System._hardware.append(HeavyHardware(name, cap, mem))

    @staticmethod
    def register_express_software(hard_name, name, cap, mem):
        for i in System._hardware:
            if hard_name == i.name:
                soft = ExpressSoftware(name, cap, mem)
                i.install(soft)
                System._software.append(soft)
                break
        else:
            return 'Hardware does not exist'

    @staticmethod
    def register_light_software(hard_name, name, cap, mem):
        for i in System._hardware:
            if hard_name == i.name:
                soft = LightSoftware(name, cap, mem)
                i.install(soft)
                System._software.append(soft)
                break
        else:
            return 'Hardware does not exist'

    @staticmethod
    def release_software_component(hard_name, soft_name):
        removed = False
        for hard in System._hardware:
            if hard.name == hard_name:
                for soft in hard.software_components:
                    if soft.name == soft_name:
                        hard.uninstall(soft)
                        System._software.remove(soft)
                        removed = True
        if not removed:
            return 'Some of the components do not exist'

    @staticmethod
    def analyze():
        res = 'System Analysis\n'
        res += f'Hardware Components: {len(System._hardware)}\n'
        res += f'Software Components: {len(System._software)}\n'
        mem_cons_all_soft = 0
        mem_cons_all_hard = 0
        for i in System._software:
            mem_cons_all_soft += i.memory_consumption
        for i in System._hardware:
            mem_cons_all_hard += i.memory
        res += f'Total Operational Memory: {mem_cons_all_soft} / {mem_cons_all_hard}\n'
        cap_cons_all_soft = 0
        cap_cons_all_hard = 0
        for i in System._software:
            cap_cons_all_soft += i.capacity_consumption
        for i in System._hardware:
            cap_cons_all_hard += i.capacity
        res += f'Total Capacity Taken: {cap_cons_all_soft} / {cap_cons_all_hard}'
        return res

    @staticmethod
    def system_split():
        res = ''
        for i in System._hardware:
            res += f'Hardware Component - {i.name}\n'
            express_count = 0
            light_count = 0
            all_soft_mem = 0
            all_soft_cap = 0
            for j in i.software_components:
                if j.software_type == 'Light':
                    light_count += 1
                else:
                    express_count += 1
                all_soft_mem += j.memory_consumption
                all_soft_cap += j.capacity_consumption
            res += f'Express Software Components: {express_count}\n'
            res += f'Light Software Components: {light_count}\n'
            res += f'Memory Usage: {all_soft_mem} / {i.memory}\n'
            res += f'Capacity Usage: {all_soft_cap} / {i.capacity}\n'
            res += f'Type: {i.hardware_type}\n'
            if len(i.software_components) > 0:
                res += f'Software Components: {", ".join(x.name for x in i.software_components)}\n'
            else:
                res += 'Software Components: None\n'
        return res[0: len(res) - 1]
