class Varastossa:
    def __init__(self) -> None:
        pass

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Alennuskoodi:
    def __init__(self, name, prossa):
        self.name = name
        self.prossa = prossa

class VoimassaOlevatKoodit:
    def __init__(self) -> None:
        self.koodit = []

    def lisaa_koodi(self, koodi):
        self.koodit.append(koodi)


class ShoppingCart:

    def __init__(self) -> None:
        self.tuotteet = []
        self.kokonaishinta = 0
        self.alennuskoodit = []

    def lisaa_tuote(self, tuote, montako = 1):
        for x in range(montako):
            self.tuotteet.append(tuote)
            self.kokonaishinta += tuote.price

    def poista_tuote(self, tuote):
        self.tuotteet.remove(tuote)
        self.kokonaishinta -= tuote.price

    def lisaa_alennuskoodi(self, koodi, koodit):
        if koodi in koodit.koodit:
            self.alennuskoodit.append(koodi)
        else:
            print("ei voimassa")

    def nayta_alennuskoodit(self):
        for koodi in self.alennuskoodit:
            print(koodi.name)        

    def poista_alennuskoodi(self, koodi):
        self.tuotteet.remove(koodi)

    def kerro_hinta(self):
        alennukset = sum([koodiolio.prossa for koodiolio in self.alennuskoodit])
        print("alennukset yhteensä", alennukset, "%")
        if alennukset > 0:
            print(self.kokonaishinta  - (self.kokonaishinta * ( alennukset / 100)))
        else:
            print(self.kokonaishinta)

    def maksa(self):
        print("Millä maksat? Vaihtoehdot: MobilePay ja luottokortti")


pc1 = Item("pc1", 1000)
pc2 = Item("pc2", 2000)
naytto = Item("naytto", 400)  
laku = Item("laku", 2)  
tanaan = Alennuskoodi("ALE161124", 6)
eilen = Alennuskoodi("ALE151124", 5)
blackf = Alennuskoodi("BLACKF", 10)

koodit = VoimassaOlevatKoodit()
koodit.lisaa_koodi(tanaan)
koodit.lisaa_koodi(blackf)

kori = ShoppingCart()
kori.lisaa_tuote(pc1) # default 1 kpl
kori.lisaa_tuote(naytto)
kori.kerro_hinta()
kori.poista_tuote(pc1)
kori.kerro_hinta()
kori.lisaa_tuote(laku, 10)   # 10 kpl
kori.kerro_hinta()
kori.lisaa_alennuskoodi(eilen, koodit)
kori.nayta_alennuskoodit()
kori.lisaa_alennuskoodi(blackf, koodit)
kori.nayta_alennuskoodit()
kori.kerro_hinta()
kori.lisaa_alennuskoodi(tanaan, koodit)
kori.nayta_alennuskoodit()
kori.kerro_hinta()
kori.maksa()


