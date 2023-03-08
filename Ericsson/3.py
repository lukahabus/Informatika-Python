class MilesToKm:
    def get_miles_to_km(self):
        return 1.6069

    def miles_to_km(self, miles):
        return self.get_miles_to_km() * miles

class NauticalMiles(MilesToKm):
    def get_miles_to_km(self):
        return 1.852
    