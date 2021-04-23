from functools import reduce    # "flatten":ia varten
import datetime  

class Kiipeilyreitti:
    """ vanha:
    def __init__(self, nimi: str, pituus: int, grade: str, ticks = 0):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade
        self.onko_kiivetty = False    
        self.tikkauspvm = None    
        self.ticks = ticks """

    def __init__(self, data:list):
        self.raakadata = data
        self.nimi = data[0]
        self.pituus =  int(data[1])
        self.grade =  data[2]
        self.ticks =  int(data[3])       
        self.onko_kiivetty = False
        self.onkokiivetty()        
        self.tikkauspvm = None   
        self.grade_opinion = None
        self.rating = None
        self.sport_vai_tradi = int(data[4])
        self.attribuutit = [self.nimi, self.pituus, self.grade, self.ticks, self.sport_vai_tradi]         # HUOM !!!!!
                               # 0           1           2            3           4

    def __gt__(self, verrokki):
        return self.nimi > verrokki.nimi

    def anna_grade_opinion (self, grade):
        self.grade_opinion = grade

    def anna_rating (self, rating):
        self.rating = rating
     

    def onkokiivetty(self):
        if len(self.raakadata) == 6:
            self.onko_kiivetty = True
        else:
            self.onko_kiivetty = False

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
        self.__reitit = []

    def lisaa_reitti(self, reitti: Kiipeilyreitti):
        self.__reitit.append(reitti)

    def reitteja(self):
        return len(self.__reitit)

    def reitit_graden_mukaan(self, grade):
        reitit = [(self.nimi, reitti) for reitti in self.__reitit if reitti.grade== grade]        
        return reitit

    def kiivetyt(self):
        return [(self.nimi, reitti) for reitti in self.__reitit if reitti.onko_kiivetty == True]        
         
    def kiipeamattomat(self):
        return [(self.nimi, reitti) for reitti in self.__reitit if reitti.onko_kiivetty == False]        

    def vaikein_reitti(self):
        def vaikeuden_mukaan(reitti):
            return reitti.grade, reitti.pituus     ###  HUOM !!!!  Järjestäminen 2 parametrin mukaan
        return sorted(self.__reitit, key=vaikeuden_mukaan)[-1]

    def __str__(self):
        return f"{self.nimi} {self.reitteja()} reittiä, vaikein {self.vaikein_reitti().grade}({self.vaikein_reitti().nimi})"


########################################################################################################

kalliot = []

def openfile():
    f = open("data.txt", "r")
    data = [rivi.strip().split(",") for rivi in f] 
    for item in data:  
        if len(item) == 1:            
            kalliot.append(Kiipeilykallio(reduce(lambda x,y: x+y, item)))    # poistaa []
        else:
            kalliot[-1].lisaa_reitti(Kiipeilyreitti(item))
    print(kalliot[-1])
    print(kalliot[-1].kiivetyt())

def etsi_tietyn_greidin_reitit(kalliot:list, grade):
    # tähän tulee yhdet sulkuparit liikaa
    #vastaus_lista = [kallio.reitit_graden_mukaan(grade) for kallio in kalliot if kallio.reitit_graden_mukaan(grade) != []]
    
    for kallio in kalliot:        
        vastaus_lista = kallio.reitit_graden_mukaan(grade)
        for kallion_nimi, reitti in vastaus_lista:
           print(kallion_nimi, ": " ,  reitti)
           
    #return sorted(kalliot, key=lambda kallio: kallio.reitit_graden_mukaan(grade))   
    # tämä ei sovelias, koska ei haluata palauttaa kaikkia kallioita: ei välttis ole tiettyä greidiä

def kiivetyt_greidin_mukaan(kalliot:list):
    vastaus_lista = []
    for kallio in kalliot:        
        vastaus_lista.append(kallio.kiivetyt())
    vastaus_lista = reduce(lambda x,y: x+y,vastaus_lista)    # flatten = [1,2,3],[4,5,6], [7] --> [1, 2, 3, 4, 5, 6, 7]
    #print(vastaus_lista)                # (self.nimi, reitti)
    return sorted(vastaus_lista, key=lambda kallio: kallio[1].grade)  



def kiivetyt_aikajarjestyksessa(kalliot:list):   
    vastaus_lista = []
    for kallio in kalliot:        
        vastaus_lista.append(kallio.kiivetyt())
    vastaus_lista = reduce(lambda x,y: x+y,vastaus_lista)    # flatten = [1,2,3],[4,5,6], [7] --> [1, 2, 3, 4, 5, 6, 7]
    #print(vastaus_lista)                # (self.nimi, reitti)
    return sorted(vastaus_lista, key=lambda kallio: kallio[1].tikkauspvm)  



def kiipeamattomat_anna_greidi_saa_tikit(kalliot:list, greidi):
    vastaus_lista = []
    for kallio in kalliot:        
        vastaus_lista.append(kallio.kiipeamattomat())
    vastaus_lista = reduce(lambda x,y: x+y,vastaus_lista)    # flatten = [1,2,3],[4,5,6], [7] --> [1, 2, 3, 4, 5, 6, 7]
    #print(vastaus_lista)                # (self.nimi, reitti)
    oikeagreidiset = [kallio for kallio in vastaus_lista if kallio[1].grade == greidi]
    return sorted(oikeagreidiset, key=lambda kallio: kallio[1].ticks, reverse = True)   


def reittien_maaran_mukaan(kalliot:list):
    return sorted(kalliot, key=lambda kallio: kallio.reitteja())   

def vaikeimman_reitin_mukaan(kalliot:list):
    #return list(reversed(vaikeuden_mukaan[kallio for kallio.vaikein_reitti() in kalliot])
    return sorted(kalliot, key=lambda kallio: kallio.vaikein_reitti().grade, reverse = True)   



 

if __name__ == "__main__":

    openfile()

    """
    k1 = Kiipeilykallio("Olhava")
    kantti = Kiipeilyreitti("Kantti", 38, "6A+", 31)
    k1.lisaa_reitti(kantti)
    kantti.tikkaa()
    k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B", 21))
    k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+", 55))


    k2 = Kiipeilykallio("Nummi")
    k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))
    k2.lisaa_reitti(Kiipeilyreitti("PidempiSyncro", 15, "8C+"))

    nalkkila = Kiipeilykallio("Nalkkilan släbi")
    nalkkila.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+", 61))
    nalkkila.lisaa_reitti(Kiipeilyreitti("Smooth operator", 11, "7A", 11))
    possu = Kiipeilyreitti("Possu ei pidä", 12 , "6B+", 45)
    nalkkila.lisaa_reitti(possu)
    possu.tikkaa()
    hedelma = Kiipeilyreitti("Hedelmätarha", 8, "6A", 88)
    nalkkila.lisaa_reitti(hedelma)
    print(hedelma.nimi, hedelma.tikkausvuosi())
    hedelma.tikkaa()
    print(hedelma.nimi, hedelma.tikkausvuosi())
    niinanErikoinen = Kiipeilyreitti("Niinan erikoinen", 28, "6A+", 77)
    nalkkila.lisaa_reitti(niinanErikoinen)
    
    print("vaikein_reitti:", nalkkila.vaikein_reitti())

    print(k1)
    print(nalkkila.nimi, nalkkila.reitteja())
    print(nalkkila.vaikein_reitti())
    kalliot = [k1, k2, nalkkila]
    print()
    for kallio in reittien_maaran_mukaan(kalliot):
        print(kallio)

    print()
    for kallio in vaikeimman_reitin_mukaan(kalliot):
        print(kallio)

    print("\netsi_tietyn_greidin_reitit:")
    etsi_tietyn_greidin_reitit(kalliot, "6A+")

    print("\nkiivetyt_greidin_mukaan:")    
    for kallion_nimi, reitti in kiivetyt_greidin_mukaan(kalliot):
        print(kallion_nimi, ": " ,  reitti)
       
    print("\nkiipeamättomat_anna_greidi_saa_tikit:")
    for kallion_nimi, reitti in kiipeamattomat_anna_greidi_saa_tikit(kalliot, "6A+"):
        print(kallion_nimi, ": " ,  reitti)

    niinanErikoinen.tikkaa()
    print( niinanErikoinen.tikkausvuosi())

    print("\nkiipeamattomat_anna_greidi_saa_tikit:")
    for kallion_nimi, reitti in kiipeamattomat_anna_greidi_saa_tikit(kalliot, "6A+"):
        print(kallion_nimi, ": " ,  reitti)

    print("\nkiipeamattomat @ Nalkkila:")
    for kallion_nimi, reitti in nalkkila.kiipeamattomat():
        print(reitti)

    print("\nkiivetyt_aikajarjestyksessa:")
    for kallion_nimi, reitti in kiivetyt_aikajarjestyksessa(kalliot):
        print(reitti)

    pvm = datetime.datetime.strptime("2020-06-07", '%Y-%m-%d')
    niinanErikoinen.tikkauspvm = pvm
    print("\nkiivetyt_aikajarjestyksessa:")
    for kallion_nimi, reitti in kiivetyt_aikajarjestyksessa(kalliot):
        print(reitti, reitti.pvm())
    """