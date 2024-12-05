class Airport:
    index = 0

    def __init__(self, airport_name, iso_country,  municipality, country, ident, latitude_deg, longitude_deg):
        self.id = Airport.index + 1
        Airport.index = Airport.index + 1
        self.airport_name = airport_name
        self.iso_country = iso_country
        self.municipality = municipality
        self.country = country
        self.ident = ident
        self.latitude_deg = latitude_deg
        self.longitude_deg = longitude_deg

    def combine_details(self):
        return {'ID': self.id,
                'airport': self.airport_name,
                'iso_country': self.iso_country,
                'municipality': self.municipality,
                'country': self.country,
                'ident': self.ident,
                'latitude_deg': self.latitude_deg,
                'longitude_deg': self.longitude_deg}