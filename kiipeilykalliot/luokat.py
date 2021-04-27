from functools import reduce    # "flatten":ia varten
import datetime  

class Kiipeilyreitti:
    
    def __init__(self, data:list):
        self.raakadata = data
        self.sanakirja = {}
        self.kasittele_attribuutit()        
        self.nimi = self.sanakirja["nimi"]           # nämä ei välttämättömät mutta lyhyempi merkintä kuin sanakirja["x"]
        self.pituus = self.sanakirja["pituus"]   
        self.grade =  self.sanakirja["grade"]
        self.ticks =  int(self.sanakirja["ticks"])         
        self.type = self.sanakirja["type"]
        self.tick = self.sanakirja["tick"]   # yes / no
        self.onkokiivetty()                  # -->  True/ False
        self.tikkauspvm = None   
        self.grade_opinion = None
        self.rating = None

    
    def kasittele_attribuutit(self):
        for pari in self.raakadata:
            self.sanakirja[pari[0]]= pari[1]
        print(self.sanakirja)

    def onkokiivetty(self):
        if self.sanakirja["tick"] == "yes":
            self.sanakirja["tick"] = True
        else:
            self.sanakirja["tick"] = False
    
    def __gt__(self, verrokki):
        return self.nimi > verrokki.nimi

    def anna_grade_opinion (self, grade):
        self.grade_opinion = grade

    def anna_rating (self, rating):
        self.rating = rating    

    def tikkaa(self):
        self.tick = True
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

    def jarjesta_reitit_yhden_attribuutin_mukaan(self, minka_mukaan):
        def yhden_mukaan(reitti):
            return reitti.sanakirja[minka_mukaan]
        return sorted(self.reitit, key=yhden_mukaan)

    def jarjesta_reitit_kahden_attribuutin_mukaan(self, minka_mukaan1, minka_mukaan2):
        def kahden_mukaan(reitti):
            return reitti.sanakirja[minka_mukaan1], reitti.sanakirja[minka_mukaan2]
        return sorted(self.reitit, key=kahden_mukaan)

    def etsi_reitit_yhden_attribuutin_mukaan(self, mika_attribuutti, mita_etsitaan):
        reitit = [(self.nimi, reitti) for reitti in self.reitit if reitti.sanakirja[mika_attribuutti] == mita_etsitaan]        
        return reitit

    def lisaa_reitti(self, reitti: Kiipeilyreitti):
        self.reitit.append(reitti)

    def reitteja(self):
        return len(self.reitit)  

    def kiivetty_lkm(self):
        return len([reitti for reitti in self.reitit if reitti.sanakirja["tick"] == True])  

    def __str__(self):
        return f"{self.nimi} {self.reitteja()} reittiä, joista kiivetty {self.kiivetty_lkm()}"


########################################################################################################