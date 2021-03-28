class Kokonaistulos:

    def __init__(self, nimi, speed):   # speed-kilpailu on ekana
        self.nimi = nimi
        self.speed = speed   # monenneksiko tyyppi tuli tässä lajissa

    def lisaa_boulder (self, boulder):
        self.boulder = boulder

    def lisaa_lead(self, lead):
        self.lead = lead

    def yhteispisteet(self):
        return self.speed * self.boulder * self.lead 

    def voitot(self):
        #print( [self.speed, self.boulder, self.lead].count(1))
        return  [self.speed, self.boulder, self.lead].count(1)

    def __str__(self):
        return f"speed:{self.speed}, boulder:{self.boulder}, lead:{self.lead}"