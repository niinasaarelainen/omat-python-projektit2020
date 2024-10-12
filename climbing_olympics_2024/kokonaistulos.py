class Kokonaistulos:

    def __init__(self, kilpailija):   # speed-kilpailu on ekana
        self.nimi = kilpailija.nimi
        self.kilpailija = kilpailija
        self.karsinnan_sij = None

    def lisaa_boulder (self, boulder):
        self.boulder = boulder

    def lisaa_lead(self, lead):
        self.lead = lead

    def yhteispisteet(self):
        return self.speed * self.boulder * self.lead 

    def voitot(self):   # jos tasapisteet, ensisijainen kriteeri
        return  [self.speed, self.boulder, self.lead].count(1)

    def paras_sijoitus(self):  # jos tasapisteet, toissijainen kriteeri
        return min(self.boulder, self.lead) 

    def karsinnansijoitus(self):
        return self.karsinnan_sij

    def __str__(self):
        return f"boulder:{self.boulder}, lead:{self.lead}"