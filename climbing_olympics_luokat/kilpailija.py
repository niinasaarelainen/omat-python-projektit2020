class Kilpailija:

    def __init__(self, nimi):
        self.nimi = nimi
        self.pituus = None
        self.paino = None
        self.wingspan = None
        self.maa = None
        self.ika = None

    def anna_muut_tiedot(self, pituus, paino, wingspan, maa, ika):
        self.pituus = pituus
        self.paino = paino
        self.wingspan = wingspan
        self.maa = maa
        self.ika = ika

    def __str__(self):
        