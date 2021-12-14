"""
def kay_lapi(solmu, polku):
    if solmu=='pieniKirjain' and solmu in polku:
        return

    if solmu=='end':
        print('->'.join(polku))
        pass

    for s in solmu.seuraavat:
        kay_lapi(s, polku+s)

kay_lapi('start',[])   """



class Tyontekija:
    def __init__(self, nimi: str):
        self.nimi = nimi
        self.alaiset = []

    def lisaa_alainen(self, tyontekija: 'Tyontekija'):
        self.alaiset.append(tyontekija)


def laske_alaiset(tyontekija: Tyontekija):
    if tyontekija.alaiset == []:   
        return 0

    summa = len(tyontekija.alaiset)
    for alainen in tyontekija.alaiset:
        print(alainen.nimi)
        summa +=  laske_alaiset(alainen) 

    return summa




if __name__ == "__main__":
    t1 = Tyontekija("Sasu")
    t2 = Tyontekija("Erkki")
    t3 = Tyontekija("Matti")
    t4 = Tyontekija("Emilia")
    t5 = Tyontekija("Antti")
    t6 = Tyontekija("Kjell")
    
    t1.lisaa_alainen(t6)    # "Kjell"
    t1.lisaa_alainen(t4)   # "Emilia"
    t4.lisaa_alainen(t2)    # "Erkki"
    t4.lisaa_alainen(t3)   # "Matti"
    t4.lisaa_alainen(t5)

    t3.lisaa_alainen(Tyontekija("Alaisen alaisen alainen"))   # Matin, Emilian ja Sasun alainen

    print("\nt1:")
    print(laske_alaiset(t1))   #6
    print("\nt4:")
    print(laske_alaiset(t4))   #3
    print("\nt5:")
    print(laske_alaiset(t5))   #0

    