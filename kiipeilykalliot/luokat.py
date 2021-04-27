from functools import reduce    # "flatten":ia varten
import datetime  

class Kiipeilyreitti:
    
    def __init__(self, data:list):
        self.raakadata = data
        self.sanakirja = {}
        self.kasittele_attribuutit()        
        self.nimi = self.sanakirja["nimi"]        
        self.pituus =  int(self.sanakirja["pituus"])
        self.grade =  self.sanakirja["grade"]
        self.ticks =  self.sanakirja["ticks"]  
        self.tick = self.sanakirja["tick"]   # True/ False
        self.onkokiivetty()        
        self.tikkauspvm = None   
        self.grade_opinion = None
        self.rating = None
        self.type = self.sanakirja["type"]
        self.attribuutit = [self.nimi, self.pituus, self.grade, self.ticks, self.type]         # HUOM !!!!!
                               # 0           1           2            3           4
    
    def kasittele_attribuutit(self):
        for pari in self.raakadata:
            self.sanakirja[pari[0]]= pari[1]
        print(self.sanakirja)
    
    def __gt__(self, verrokki):
        return self.nimi > verrokki.nimi

    def anna_grade_opinion (self, grade):
        self.grade_opinion = grade

    def anna_rating (self, rating):
        self.rating = rating
     

    def onkokiivetty(self):
        if self.tick == "yes":
            self.tick = True
        else:
            self.tick = False

    def tikkaa(self):
        self.onko_kiivetty = True
        self.tikkauspvm = datetime.datetime.today()
        self.ticks += 1

    def tikkausvuosi (self):
        if self.tikkauspvm == None:
            return "Ei ole kiivetty"
        return self.tikkauspvm.year

    def pvm(self):
        if self.tikkauspvm == None:
            return "Ei ole kiivetty"
        return f"  tikattu: {self.tikkauspvm.day}.{self.tikkauspvm.month}.{self.tikkauspvm.year}"

    def __str__(self):
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}, ticks {self.ticks}"

########################################################################################################
class Kiipeilykallio:
    def __init__(self, nimi: str):
        self.nimi = nimi
        self.reitit = []


    def jarjesta_reitit_yhden_attribuutin_mukaan(self, nro):
        def yhden_mukaan(reitti):
            return reitti.attribuutit[nro]     
        return sorted(self.reitit, key=yhden_mukaan)

    def jarjesta_reitit_kahden_attribuutin_mukaan(self, nro1, nro2):
        def kahden_mukaan(reitti):
            return reitti.attribuutit[nro1], reitti.attribuutit[nro2]     
        return sorted(self.reitit, key=kahden_mukaan)


    def lisaa_reitti(self, reitti: Kiipeilyreitti):
        self.reitit.append(reitti)

    def reitteja(self):
        return len(self.reitit)

    def reitit_graden_mukaan(self, grade):
        reitit = [(self.nimi, reitti) for reitti in self.reitit if reitti.grade== grade]        
        return reitit

    def kiivetyt(self):
        return [(self.nimi, reitti) for reitti in self.reitit if reitti.onko_kiivetty == True]        
         
    def kiipeamattomat(self):
        return [(self.nimi, reitti) for reitti in self.reitit if reitti.onko_kiivetty == False]        

    def vaikein_reitti(self):
        def vaikeuden_mukaan(reitti):
            return reitti.grade, reitti.pituus     ###  HUOM !!!!  Järjestäminen 2 parametrin mukaan
        return sorted(self.reitit, key=vaikeuden_mukaan)[-1]

    def __str__(self):
        return f"{self.nimi} {self.reitteja()} reittiä, vaikein {self.vaikein_reitti().grade}({self.vaikein_reitti().nimi})"


########################################################################################################