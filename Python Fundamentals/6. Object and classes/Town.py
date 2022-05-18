class Town:
    def __init__(self, name, latitude='O°E', longitude='0°N'):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        a = f'Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}'
        return a
