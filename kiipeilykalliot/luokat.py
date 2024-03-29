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
        print(" 2 = Mikä sijainti Suomessa")
        print(" 3 = Printtaa tietyn kallion reittistatistiikka")
        print(" 4 = Etsi kallion reiteistä hakusanalla") 
        print(" 5 = Printtaa kallion kaikki reitit") 
        self.kalliovalinta = input("Valitse 1 - 5  ")
        return self.kalliovalinta

    def reittiValinnat(self):
        print("\n 1 = Etsi")
        print(" 2 = Järjestä")
        print(" 3 = Tikkaa")
        print(" 4 = Merkkaa projektiksi")
        print(" 5 = Grade-mielipide")
        print(" 6 = Arvostele reitti")
        print(" 7 = Näytä reitin henk.koht. tiedot")
        self.reittivalinta = input("Valitse 1 - 7  ")
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
        # tähän asti löytyy data.txt, tästä eteenpäin data_henkkoht.txt  
        self.sanakirja["tick"] = "False"
        self.sanakirja["tikkauspvm"] = None
        self.sanakirja["projektina"] = "False"
        self.sanakirja["grade_opinion"] = "-"
        self.sanakirja["rating"] = "-1"

    
    def kasittele_attribuutit(self):
        for pari in self.raakadata:
            if pari[0] == "ticks":
                self.sanakirja[pari[0]]= int(pari[1]) #jos ei tee int(), järjestää esim. 1, 11, 3, 33, 4...
            else:
                self.sanakirja[pari[0]]= pari[1]
        if "sektori" not in self.sanakirja:
             self.sanakirja["sektori"] = ""
        #print(self.sanakirja)

    def kasittele_luontipvm(self):
        osat = self.luontipvm.split(".")
        self.luontipvm = date(int(osat[2]), int(osat[1]), int(osat[0]))

    def print_luontipvm(self):
        return f"{self.luontipvm.day}.{self.luontipvm.month}.{self.luontipvm.year}"
    
    def __gt__(self, verrokki):
        return self.nimi > verrokki.nimi

    def anna_grade_opinion (self, grade):
        self.sanakirja["grade_opinion"] = grade

        f = open("data_henkkoht.txt", "a")
        f.write(self.nimi + " grade_opinion " + self.sanakirja["grade_opinion"] + "\n")
        f.close

    def anna_rating (self, rating):
        self.sanakirja["rating"] = rating
        print(self.nimi, self.sanakirja["rating"])

        f = open("data_henkkoht.txt", "a")
        f.write(self.nimi+ " rating " + self.sanakirja["rating"] + "\n")
        f.close

    def tikkaa(self):
        self.sanakirja["tick"] = "True"   # rwkarifailista luetaan tekstiä, ei boolean
        self.sanakirja["tikkauspvm"] = str(datetime.datetime.today()).split(" ")[0]
        self.ticks += 1
        self.projektina = "False"  

        f = open("data_henkkoht.txt", "a")
        f.write(self.nimi+ " tick " + self.sanakirja["tick"] + "\n")
        f.write(self.nimi+ " tikkauspvm " + self.sanakirja["tikkauspvm"] + "\n")
        f.write(self.nimi+ " projektina " + self.sanakirja["projektina"] + "\n")
        f.close

    def nayta_henk_koht_tiedot(self):
        rating = self.sanakirja["rating"]
        if rating == "-1":
            rating = "-"
        grade_opinion = self.sanakirja["grade_opinion"]
        return f"{self.nimi}: {self.tikkausvuosi()}, {self.projekti()}, greidi noinniinku omasta mielestä: {grade_opinion}, arvosana: {rating}"

    def tikkausvuosi (self):
        tikkauspvm = self.sanakirja["tikkauspvm"]
        if tikkauspvm == None:
            return "Ei ole kiivetty"
        return f"kiivetty {tikkauspvm}"

    def projektina (self):
        self.sanakirja["projektina"] = "True"
        print(self.nimi + " on nyt projektisi")

        f = open("data_henkkoht.txt", "a")
        f.write(self.nimi+ " projektina " + self.sanakirja["projektina"] + "\n")
        f.close

    def projekti(self):
        if  self.sanakirja["projektina"] == "False":
            return "ei työn alla"
        return "projektina"

    def pvm(self):
        tikkauspvm = self.sanakirja["tikkauspvm"]
        if tikkauspvm == None:
            return "Ei ole kiivetty"
        return f"  tikattu: {tikkauspvm}"

    def __str__(self):
        rating = self.sanakirja["rating"]
        if self.sanakirja["rating"] != "-1":
            return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}, ticks {self.ticks}, oma arvosana {rating} ({self.kallio})"
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}, ticks {self.ticks} ({self.kallio})"


########################################################################################################
class Kiipeilykallio:
    def __init__(self, nimi, ilmansuunta, sijainti: str):
        self.nimi = nimi
        self.ilmansuunta = ilmansuunta
        self.sijainti = sijainti
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
        palautus_str = "\n" + self.nimi + "n reitit greidijärjestyksessä:\n"
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
        return len([reitti for reitti in self.reitit if reitti.sanakirja["tick"] == "True"])  

    def __str__(self):
        return f"\n{self.nimi} {self.reitteja()} reittiä, joista kiivetty {self.kiivetty_lkm()}\n{self.grade_statistics()}"


########################################################################################################