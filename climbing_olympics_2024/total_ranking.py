import speed, boulder, lead, kokonaistulos, pygame
from operator import itemgetter

class Kilpailija:

    def __init__(self, nimi, pituus, paino, wingspan, maa, ika, ranking = "-"):
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.wingspan = wingspan
        self.maa = maa
        self.ika = ika
        self.ranking = ranking

    def painotukset(self, s, b, l):  # arvosana 1-10 kunkin disciplinen taidoista, 10 = maailman paras
        self.s = s
        self.b = b
        self.l = l

    def __str__(self):
        if self.wingspan > 0:                                                 # halutaan plusmerkki näkyviin
            return f"\n{self.nimi} ({self.maa})\n {self.ika} years, {self.pituus} cm, wingspan +{self.wingspan}, {self.paino} kg\n best ranking in 2019: {self.ranking}"
        else:   
            return f"\n{self.nimi} ({self.maa})\n {self.ika} years, {self.pituus} cm, wingspan {self.wingspan}, {self.paino} kg\n best ranking in 2019: {self.ranking}"
        
####  end  class Kilpailija ##############################################################


def luo_kilpailijat_miehet():
    # 20 miestä olympialaisissa 2024:
    kilpailijat["Serato Anraku"] = Kilpailija("Serato Anraku", 169, 60,  "Japan", 17)    
    kilpailijat["Serato Anraku"].painotukset(6, 8, 8) # arvosana 1-10 kunkin disciplinen taidoista, 10 = maailman paras
    kilpailijat["Toby Roberts"] = Kilpailija("Toby Roberts", 178, 63, "GBR", 18)
    kilpailijat["Toby Roberts"].painotukset(4, 9, 4)
    kilpailijat["Jakob Schubert"] = Kilpailija("Jakob Schubert", 173, 63, "Austria", 33)
    kilpailijat["Jakob Schubert"].painotukset(7, 10, 9)
    kilpailijat["Tomoa Narasaki"] = Kilpailija("Tomoa Narasaki", 170, 58, "Japan", 27) 
    kilpailijat["Tomoa Narasaki"].painotukset(8, 10, 7)
    kilpailijat["Paul Jenft"] = Kilpailija("Paul Jenft", 168, 51, "France", 22)    
    kilpailijat["Paul Jenft"].painotukset(8, 10, 7) 
    kilpailijat["Colin Duffy"] = Kilpailija("Colin Duffy", 168, 55, "USA", 20) 
    kilpailijat["Colin Duffy"] .painotukset(6, 9, 8)   
    kilpailijat["Jessie Grouper"] = Kilpailija("Jessie Grouper", 182, 74, "USA", 21)
    kilpailijat["Jessie Grouper"].painotukset(8, 10, 6)
    kilpailijat["Adam Ondra"] = Kilpailija("Adam Ondra", 186, 70, "Czeck", 31) 
    kilpailijat["Adam Ondra"].painotukset(4, 10, 10)
    kilpailijat["Janeck Flohe"] = Kilpailija("Janeck Flohe", 188, 77, "Germany", 26)
    kilpailijat["Janeck Flohe"].painotukset(6, 7, 8)
    kilpailijat[""] = Kilpailija("", 177, 66, -2, "", 25) 
    kilpailijat[""].painotukset(10, 2, 2)
    kilpailijat["Sam Avezou"] = Kilpailija("Sam Avezou", 177, 68,  "France", 30) 
    kilpailijat["Sam Avezou"].painotukset(7, 10, 5)
    kilpailijat["Alexander Megos"] = Kilpailija("Alexander Megos", 173, 57,  "Germany", 28) 
    kilpailijat["Alexander Megos"].painotukset(6, 8, 8)
    kilpailijat[" "] = Kilpailija("", 177, 68, "Italy", 24) 
    kilpailijat[""].painotukset(10, 2, 2)
    kilpailijat[""] = Kilpailija("", 177, 62,  "Italy", 25)
    kilpailijat[""].painotukset(3, 7, 6)
    kilpailijat["Dohyan Lee"] = Kilpailija("Dohyan Lee", 176, 53, "South Korea", 25)
    kilpailijat["Dohyan Lee"].painotukset(8, 10, 7)
    kilpailijat[""] = Kilpailija("", 177, 71, 2, "", 36)
    kilpailijat[""] .painotukset(10, 4, 5)
    kilpailijat["Alberto Ginéz López"] = Kilpailija("Alberto Ginéz López", 169, 58, "Spain", 18)
    kilpailijat["Alberto Ginéz López"].painotukset(9, 6, 10)
    kilpailijat[""] = Kilpailija("", 177, 62,  "Australia", 28)
    kilpailijat[""].painotukset(8, 3, 4)
    kilpailijat["Christopher Cosser"] = Kilpailija("Christopher Cosser", 177, 71,  "South Africa", 20)
    kilpailijat["Christopher Cosser"].painotukset(2, 2, 3)
    kilpailijat["YuFei Pan"] = Kilpailija("YuFei Pan", 170, 59, "China", 20)
    kilpailijat["YuFei Pan"].painotukset(5, 5, 8)


def luo_kilpailijat_naiset():
    # 20 naista olympialaisissa 2024:
    kilpailijat["Janja Garnbret"] = Kilpailija("Janja Garnbret", 164, 1, "Slovenia", 22)    
    kilpailijat["Janja Garnbret"].painotukset(7, 10, 10)
    kilpailijat["Mia Krampl"] = Kilpailija("Mia Krampl", 163,  2, "Slovenia", 20)
    kilpailijat["Mia Krampl"].painotukset(6, 9, 9)
    kilpailijat["Jessica Pilz"] = Kilpailija("Jessica Pilz", 163,  -2, "Austria", 24) 
    kilpailijat["Jessica Pilz"].painotukset(6, 9, 9)
    kilpailijat[""] = Kilpailija("", 165,  12, "Switzerland", 29) 
    kilpailijat[""].painotukset(5, 8, 6)
    kilpailijat[""] = Kilpailija("", 166,  2, "France", 24)     
    kilpailijat[""].painotukset(6, 9, 6)
    kilpailijat[""] = Kilpailija("", 163,  2, "France", 24)
    kilpailijat[""].painotukset(10, 2, 2)
    kilpailijat["Miho Nonaka"] = Kilpailija("Miho Nonaka", 162,  2, "Japan", 23) 
    kilpailijat["Miho Nonaka"].painotukset(9, 10, 6)
    kilpailijat[""] = Kilpailija("", 165, 2, "Japan", 31) 
    kilpailijat[""].painotukset(7, 9, 9)
    kilpailijat[""] = Kilpailija("", 166,  2, "Canada", 27) 
    kilpailijat[""].painotukset(6, 9, 6)
    kilpailijat["Brooke Raboutou"] = Kilpailija("Brooke Raboutou", 154, 3, "USA", 20) 
    kilpailijat["Brooke Raboutou"].painotukset(7, 10, 8)
    kilpailijat[""] = Kilpailija("", 162,  2, "USA", 24) 
    kilpailijat[""].painotukset(7, 9, 9)
    kilpailijat[""] = Kilpailija("", 163,  2, "Great Britain", 24) 
    kilpailijat[""].painotukset(5, 9, 7)
    kilpailijat[""]  = Kilpailija("", 163,  2, "Poland", 27)
    kilpailijat[""].painotukset(10, 2, 2)
    kilpailijat["Chaehyun Seo"] = Kilpailija("Chaehyun Seo", 160,  2, "South Korea", 17)
    kilpailijat["Chaehyun Seo"].painotukset(5, 8, 10)
    kilpailijat[""] = Kilpailija("", 163,  2, "Russia", 28)
    kilpailijat[""].painotukset(10, 3, 3)
    kilpailijat[""] = Kilpailija("", 163,  2, "Russia", 20)
    kilpailijat[""].painotukset(6, 8, 9)
    kilpailijat["Laura Rogora"] = Kilpailija("Laura Rogora", 163, 2, "Italia", 20)
    kilpailijat["Laura Rogora"].painotukset(7, 9, 9) 
    kilpailijat[""] = Kilpailija("", 163,  2, "China", 24)
    kilpailijat[""].painotukset(10, 3, 3)
    kilpailijat["Oceania MacKenzie"] = Kilpailija("Oceania MacKenzie", 163,  2, "Australia", 18)
    kilpailijat["Oceania MacKenzie"].painotukset(3, 5, 3)
    kilpailijat["Erin Sterkenburg"] = Kilpailija("Erin Sterkenburg", 163, 2, "South Africa", 18)
    kilpailijat["Erin Sterkenburg"].painotukset(2, 2, 1)
    

def kilpailu():
    global tulokset
    #   K A R S I N T A : 
    speedKilpailu = speed.SpeedKilpailu(voittoaika)
    sij = 1  # eka sijoitus = 1
    for tulos in speedKilpailu.speed_karsinta(kilpailijat)  :
        t = kokonaistulos.Kokonaistulos(tulos.kilpailija, sij) 
        tulokset[tulos.nimi] = t # ei tasasijoituksia
        sij += 1

    boulderKilpailu = boulder.BoulderKilpailu()
    sij = 1
    for tulos in boulderKilpailu.tulos_karsinta(kilpailijat): 
        t = tulokset[tulos.nimi]    # ei tasasijoituksia
        t.lisaa_boulder(sij)
        sij += 1

    leadKilpailu  = lead.LeadKilpailu()
    karsintatulokset = leadKilpailu.tulos_karsinta(kilpailijat)
    print("\nL E A D -- KARSINTA")
    for tulos in leadKilpailu.jarjesta_sijoitukset(karsintatulokset) :
        t = tulokset[tulos[0].nimi]    
        t.lisaa_lead(tulos[1])   # täällä saattaa olla tasasijoituksia, eri systeemi kuin speed/lead
        


    def printtaa_tulokset(karsinta_vai_finaali):
        koktulos = tulokset.values()
        if karsinta_vai_finaali == "FINAALI -- TOTAL POINTS":
            s = sorted(koktulos, key=lambda tulos: (tulos.yhteispisteet(), -tulos.voitot(), tulos.paras_sijoitus(), tulos.karsinnansijoitus))
        else:
            s = sorted(koktulos, key=lambda tulos: (tulos.yhteispisteet(), -tulos.voitot(), tulos.paras_sijoitus()))
        climber ="CLIMBER"
        lead = "LEAD"
        speed = "SPEED"
        boulder = "BOULDER"
        total = "TOTAL"
        print("\n"+karsinta_vai_finaali)
        print(f"{climber:28} {speed:<8}  {boulder:<8}  {lead:<8} {total:<8} ")
        print("-"*63)
        sijoitus = 1
        for koktulos in s:
            climber = koktulos.nimi        
            speed = koktulos.speed
            boulder = koktulos.boulder
            lead = koktulos.lead
            total = koktulos.yhteispisteet()
            print(f"{climber:28} {speed:<8}  {boulder:<8}  {lead:<8} {total:<8} ")
            koktulos.karsinnan_sij = sijoitus
            sijoitus += 1
        return s[:8]


    karsintatulos = printtaa_tulokset("KARSINTA -- TOTAL POINTS")


    #  F I N A A L I   8 PARASTA
    print("\nS P E E D -- FINAALI")
    tulokset_karsinta = tulokset
    tulokset = {}
    sij = 1  # eka sijoitus = 1
    for tulos in speedKilpailu.speed_finaali(karsintatulos, kilpailijat):    
        print(tulos) 
        t = kokonaistulos.Kokonaistulos(tulos.kilpailija, sij) 
        tulokset[tulos.nimi] = t # ei tasasijoituksia
        sij += 1

    sij = 1
    print("\nB O U L D E R -- FINAALI")
    for tulos in boulderKilpailu.tulos_finaali(karsintatulos, kilpailijat) :      
        print(tulos) 
        t = tulokset[tulos.nimi]    # ei tasasijoituksia
        t.lisaa_boulder(sij)
        sij += 1

    print("\nL E A D -- FINAALI")
    for tulos in leadKilpailu.jarjesta_sijoitukset(leadKilpailu.pisteet_finaali(karsintatulos, kilpailijat)):    
        t = tulokset[tulos[0].nimi]    
        t.lisaa_lead(tulos[1])   # täällä saattaa olla tasasijoituksia, eri systeemi kuin speed/lead        

    printtaa_tulokset("FINAALI -- TOTAL POINTS")
    palkintopalli()


def palkintopalli():
    pygame.init()
    koktulos = tulokset.values()
    s = sorted(koktulos, key=lambda tulos: (tulos.yhteispisteet(), -tulos.voitot(), tulos.paras_sijoitus(), tulos.karsinnansijoitus))
    WINDOW_HEIGHT = 410
    WINDOW_WIDTH = 900
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    fontti = pygame.font.SysFont("FreeMono", 33)
    palli = pygame.image.load('palli.jpg')
    palli = pygame.transform.scale(palli, (WINDOW_WIDTH - 40, WINDOW_HEIGHT -40))
    TEKSTIN_VARI  = (222, 22, 122)
    
    while True:   
        SCREEN.fill((249, 249, 249))  
        SCREEN.blit(palli, (0, 111))

        ekan_etunimi = s[0].nimi.split(" ")[0]
        eka = fontti.render(f"{ekan_etunimi} ", True, TEKSTIN_VARI)
        SCREEN.blit(eka, (WINDOW_WIDTH //2 - 80, 5))
        try:
            kuva = pygame.image.load("kiipeilijoiden_kuvat/" + ekan_etunimi + ".png")
            kuva = pygame.transform.scale(kuva, (105, 125))       
            SCREEN.blit(kuva, (WINDOW_WIDTH //2 - 80, 42))
        except:
            pass

        tokan_etunimi = s[1].nimi.split(" ")[0]
        toka = fontti.render(f"{tokan_etunimi} ", True, TEKSTIN_VARI)
        SCREEN.blit(toka, (108, 76))
        try:
            kuva = pygame.image.load("kiipeilijoiden_kuvat/" + tokan_etunimi + ".png")
            kuva = pygame.transform.scale(kuva, (105, 125))           
            SCREEN.blit(kuva, (108, 113))
        except:
            pass

        kolmannen_etunimi = s[2].nimi.split(" ")[0]
        kolmas = fontti.render(f"{kolmannen_etunimi} ", True, TEKSTIN_VARI)
        SCREEN.blit(kolmas, (WINDOW_WIDTH - 270, 126))
        try:
            kuva = pygame.image.load("kiipeilijoiden_kuvat/" + kolmannen_etunimi + ".png")
            kuva = pygame.transform.scale(kuva, (105, 125))       
            SCREEN.blit(kuva, (WINDOW_WIDTH - 270, 163))
        except:
            pass
           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()     
        CLOCK.tick(4)    # = 4 kertaa sekunnissa





kilpailijat = {}  # nimi : Kilpailija
tulokset =  {}   #  nimi : Kokonaistulos
voittoaika = 0.0

print("\n 1  Naisten kilpailu")
print("\n 2  Miesten kilpailu")
print("\n 3  20 naiskilpailijan tiedot")
print("\n 4  20 mieskilpailijan tiedot")
vastaus = input("\nMitä tehdään? Anna numero 1-4 ")
if vastaus == "1":
    luo_kilpailijat_naiset()
    voittoaika = 7.0  # naisten speed-maksimi
    kilpailu()
elif vastaus == "2":    
    luo_kilpailijat_miehet()
    voittoaika = 5.2 # miesten speed-maksimi
    kilpailu()
elif vastaus == "3": 
    luo_kilpailijat_naiset()
    for nimi, kilpailija in kilpailijat.items():
        print(kilpailija)
elif vastaus == "4":   
    luo_kilpailijat_miehet()
    for nimi, kilpailija in kilpailijat.items():
        print(kilpailija)  
