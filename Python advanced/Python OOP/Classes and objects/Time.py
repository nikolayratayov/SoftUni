class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def get_time(self):
        h = str(self.hours)
        m = str(self.minutes)
        s = str(self.seconds)
        if self.hours < 10:
            h = f'0{self.hours}'
        if self.minutes < 10:
            m = f'0{self.minutes}'
        if self.seconds < 10:
            s = f'0{self.seconds}'
        return f"{h}:{m}:{s}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0
        return self.get_time()
