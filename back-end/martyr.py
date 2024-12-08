class Martyr:
    def __init__(self, index, name, location, killed_enemies, trip):
        self.index = index
        self.name = name
        self.location = location
        self.killed_enemies = killed_enemies
        self.trip = trip

    def combine_details(self):
        return {'ID': self.index,
                'Name': self.name,
                'Place Of Sacrifice': self.location,
                'Killed enemies': self.killed_enemies,
                'Distance Travelled': self.trip}