class Noppa:

    def __init__(self, luku, ei_valitut, valitut):
        self.luku = luku   # 1-6
        self.valittu = False
        self.kuvat_ei_valitut = ei_valitut   # ind. 0-5
        self.kuvat_valitut = valitut
    
    def toggle_valittu(self):
        self.valittu = not self.valittu

    def kuva(self):
        if self.valittu :
            return self.kuvat_valitut[self.luku -1]
        return self.kuvat_ei_valitut[self.luku -1]