from functools import reduce    # "flatten":ia varten
import datetime  
from datetime import date


class Kayttoliittyma:

    def valinta1(self):
        print("\n 1 = Kalliot")
        print(" 2 = Reitit")
        return input("Valitse 1 tai 2  ")

    def kallioValinnat(self):
        print("\n 1 = Mikä ilmansuunta")
        print(" 2 = Printtaa tietyn kallion reitit")
        self.kalliovalinta = input("Valitse 1 tai 2  ")
        return self.kalliovalinta

    def reittiValinnat(self):
        print("\n 1 = Etsi")
        print(" 2 = Järjestä")
        self.reittivalinta = input("Valitse 1 tai 2  ")
        return self.reittivalinta
    

class Kiipeilyreitti:
    
    def __init__(self, data:list):
        self.raakadata = data
        self.sanakirja = {}
        self.kasittele_attribuutit()   
        self.kallio =  self.sanakirja["kallio"].split("#")[0]       # HUOM !!  
        self.nimi = self.sanakirja["nimi"]           # nämä ei välttämättömät mutta lyhyempi merkintä kuin sanakirja["x"]
        self.sektori = self.sanakirja["sektori"]
        self.pituus = self.sanakirja["pituus"]   
        self.grade =  self.sanakirja["grade"]
        self.ticks =  int(self.sanakirja["ticks"])      
        self.type = self.sanakirja["type"]
        self.luontipvm = self.sanakirja["luontipvm"]   # yes / no        
        self.tick = False
        self.sanakirja["tick"] = None
        self.tikkauspvm = None   
        self.sanakirja["tikkauspvm"] = None
        self.projektina = False
        self.sanakirja["projektina"] = None
        self.grade_opinion = None
        self.sanakirja["grade_opinion"] = None
        self.rating = None
        self.sanakirja["rating"] = "-1"

    
    def kasittele_attribuutit(self):
        for pari in self.raakadata:
            if pari[0] == "ticks":
                self.sanakirja[pari[0]]= int(pari[1]) #jos ei tee int(), järjestää esim. 1, 11, 3, 33, 4...
            else:
                self.sanakirja[pari[0]]= pari[1]
        if "sektori" not in self.sanakirja:
             self.sanakirja["sektori"] = ""
        print(self.sanakirja)

    def kasittele_luontipvm(self):
        osat = self.luontipvm.split(".")
        self.luontipvm = date(int(osat[2]), int(osat[1]), int(osat[0]))

    def print_luontipvm(self):
        return f"{self.luontipvm.day}.{self.luontipvm.month}.{self.luontipvm.year}"
    
    def __gt__(self, verrokki):
        return self.nimi > verrokki.nimi

    def anna_grade_opinion (self, grade):
        self.grade_opinion = grade
        self.sanakirja["grade_opinion"] = self.grade_opinion

    def anna_rating (self, rating):
        self.rating = str(rating)    
        self.sanakirja["rating"] = self.rating

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
        if self.rating != None:
            return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}, ticks {self.ticks}, oma arvosana {self.rating} ({self.kallio})"
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}, ticks {self.ticks} ({self.kallio})"


########################################################################################################
class Kiipeilykallio:
    def __init__(self, nimi, ilmansuunta: str):
        self.nimi = nimi
        self.ilmansuunta = ilmansuunta
        self.reitit = []
        self.grade_statistics_dict = {}

    def grade_statistics(self): 
        for reitti in self.reitit:
            if reitti.grade not in self.grade_statistics_dict:
                self.grade_statistics_dict[reitti.grade] = 1
            else:
                self.grade_statistics_dict[reitti.grade] += 1
        s_key = sorted(self.grade_statistics_dict.items(), key=lambda x: x[0])
        s_value = sorted(self.grade_statistics_dict.items(), key=lambda x: x[1], reverse=True)
        palautus_str = self.nimi + "n reitit greidijärjestyksessä:\n"
        for key, value in s_key:
            palautus_str += key + ": " + str(value) + "kpl, "
        palautus_str = palautus_str[:-2]
        palautus_str += "\n" + self.nimi + "n reitit yleisyysjärjestyksessä:\n"
        for key, value in s_value:
            palautus_str += key + ": " + str(value) + "kpl, "
        return palautus_str[:-2]   # vika pilkku pois


    def jarjesta_reitit_yhden_attribuutin_mukaan(self, minka_mukaan):
        print("\njärjestettiin kallion " + self.nimi + " reitit attribuutin "+ minka_mukaan + " mukaan:")   
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
        return f"\n{self.nimi} {self.reitteja()} reittiä, joista kiivetty {self.kiivetty_lkm()}\n{self.grade_statistics()}"


########################################################################################################