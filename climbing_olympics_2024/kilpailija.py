class Kilpailija:

    def __init__(self, nimi):
        self.nimi = nimi
        self.pituus = None
        self.ranking = None
        self.maa = None
        self.ika = None

    def anna_muut_tiedot(self, pituus, ranking, maa, ika):
        self.pituus = pituus
        self.ranking = ranking
        self.maa = maa
        self.ika = ika

    def __str__(self):
        if self.wingspan > 0:                                                
            return f"\n{self.nimi} ({self.maa})\n{self.ika} vuotta, {self.pituus} cm, ranking {self.ranking}"
        else:   
            return f"\n{self.nimi} ({self.maa})\n{self.ika} vuotta, {self.pituus} cm, ranking {self.ranking}"
        