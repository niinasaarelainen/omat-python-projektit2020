class Kokonaistulos:

    def __init__(self, kilpailija, speed):   # speed-kilpailu on ekana
        self.nimi = kilpailija.nimi
        self.kilpailija = kilpailija
        self.speed = speed   # monenneksiko tyyppi tuli tässä lajissa
        self.karsinnan_sij = None

    def lisaa_boulder (self, boulder):
        self.boulder = boulder

    def lisaa_lead(self, lead):
        self.lead = lead

    def yhteispisteet(self):
        return self.speed * self.boulder * self.lead 

    def voitot(self):   # jos tasapisteet, ensisijainen kriteeri
        return  [self.speed, self.boulder, self.lead].count(1)

    def yhteenlasketut_pisteet(self):  # jos tasapisteet, toissijainen kriteeri
        return self.speed + self.boulder + self.lead 

    def karsinnansijoitus(self):
        return self.karsinnan_sij

    def __str__(self):
        return f"speed:{self.speed}, boulder:{self.boulder}, lead:{self.lead}"