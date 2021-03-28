class Kokonaistulos:

    def __init__(self, nimi, speed):   # speed-kilpailu on ekana
        self.nimi = nimi
        self.speed = int(speed)

    def lisaa_boulder (self, boulder):
        self.boulder = int(boulder)

    def lisaa_lead(self, lead):
        self.lead = int(lead)

    def yhteispisteet(self):
        return self.speed * self.boulder * self.lead 

    def __str__(self):
        return f"speed:{self.speed}, boulder:{self.boulder}, lead:{self.lead}"