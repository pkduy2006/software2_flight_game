class Martyr:
    def __init__(self, id, name, location, killed_enemies):
        self.id = id
        self.name = name
        self.location = location
        self.killed_enemies = killed_enemies

    def combine_details(self):
        return {'ID': self.id,
                'Name': self.name,
                'Place Of Sacrifice': self.location,
                'Killed Enemies': self.killed_enemies}