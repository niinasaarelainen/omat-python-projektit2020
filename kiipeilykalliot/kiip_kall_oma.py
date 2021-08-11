from functools import reduce    # "flatten":ia varten
import datetime  
from luokat import *



def openfile():
    f = open("data.txt", "r")
    data = [rivi.strip().split(",") for rivi in f if rivi.strip() != ''] 
    reittilista = []
    kallion_nimi = ""
    kallio_data = []
    for rivi in data:         
        for item in rivi:   # kallio:olhava   <-- item
            pari = item.split(":")             
            if pari[0] == "kallio":   
                kallion_nimi, ilmansuunta, sijainti = pari[1].split("#")                      
                kalliot[kallion_nimi] = Kiipeilykallio(kallion_nimi, ilmansuunta, sijainti)   
                kallio_data = pari
            else:
                reittilista.append(pari)
        if reittilista != [] and kallion_nimi != '':   
            reittilista.append(kallio_data)  
            print("kallio_data", kallio_data)
            kalliot[kallion_nimi].lisaa_reitti(Kiipeilyreitti(reittilista)) 
            reittilista = []        
    kallion_nimi = ""



def muodosta_kaikki_reitit():   # häviää tieto mihin kallioon liittyvät
    kaikki_reitit = []
    for kallio in kalliot.values():
        for reitti in kallio.reitit:
            kaikki_reitit.append(reitti)
    return kaikki_reitit


def etsi_reitti_hakusanalla(hakusana):
    print("\nhakusanalla "+ hakusana + " löytyi:")
    vastaukset = []
    for kallio in kalliot.values():      # HUOM!   ei pelkkä kalliot !!!!!!!!!!!!
        for reitti in kallio.reitit:
            for value in reitti.sanakirja.values():
                if value != True and value != False and value != None:
                    if hakusana in str(value):
                       vastaukset.append(reitti)
    return vastaukset


######  J Ä R J E S T Ä  ###########
def jarjesta_reitit_yhden_attribuutin_mukaan(minka_mukaan):
    print("\njärjestettiin kaikki reitit attribuutin "+ minka_mukaan + " mukaan:")      
    def yhden_mukaan(reitti):
        return reitti.sanakirja[minka_mukaan]
    return sorted(kaikki_reitit, key=yhden_mukaan)  

def jarjesta_reitit_kahden_attribuutin_mukaan(minka_mukaan1, minka_mukaan2):
    print("\njärjestettiin kaikki reitit attribuuttien "+ minka_mukaan1 + " ja " + minka_mukaan2 + " mukaan:")    
    def kahden_mukaan(reitti):
        return reitti.sanakirja[minka_mukaan1], reitti.sanakirja[minka_mukaan2]
    return sorted(kaikki_reitit, key=kahden_mukaan)   



def kallioValinnat(valinta):
    if valinta == "1":    
        ilmansuunta = input("\n Mitä ilmansuuntaa haet?  ") 
        for kallio in kalliot.values(): 
            if ilmansuunta.upper() in kallio.ilmansuunta.upper() :
                print(kallio.nimi)
    elif valinta == "2":    
        sijainti = input("\n Kirjoita sijainti joko tarkasti esim. Lohja tai laajemmin, esim. Etelä-Suomi?  ") 
        for kallio in kalliot.values(): 
            if sijainti.upper() in kallio.sijainti.upper() :
                print(kallio.nimi)

    elif valinta == "3":           
        vaihtoehdot = ""
        print("\n Minkä kallion statistiikka printataan? Vaihtoehdot ovat:")
        for kallio in kalliot.values(): 
            vaihtoehdot += kallio.nimi + ", "
        nimi = input(" " + vaihtoehdot[:-2] + "  ")
        for kallio in kalliot.values(): 
            if nimi.upper() in kallio.nimi.upper() :
                print(kallio.grade_statistics())
    
    elif valinta == "4":           
        vaihtoehdot = ""
        print("\n Anna kallion nimi ja hakusana, voi olla osa sanasta. Kalliovaihtoehdot ovat:")
        for kallio in kalliot.values(): 
            vaihtoehdot += kallio.nimi + ", "
        hakusanat = input(" " + vaihtoehdot[:-2] + "  ")
        nimi, hakusana = hakusanat.split(" ")
        haettava_kallio = ""

        def search(lookup, reitti):
            for value in reitti.sanakirja.values():
                if lookup.upper() in str(value).upper():    # HUOM! Jotkut arvot int,  osasanat
                    return True

        for kallio in kalliot.values(): 
            if nimi.upper() in kallio.nimi.upper() :
                haettava_kallio = kallio
        reitit = [reitti for reitti in haettava_kallio.reitit if search(nimi, reitti) and search(hakusana, reitti)] 
        for reitti in reitit:
                print(reitti)
    
    elif valinta == "5":           
        vaihtoehdot = ""
        print("\n Minkä kallion reitit printataan? Vaihtoehdot ovat:")
        for kallio in kalliot.values(): 
            vaihtoehdot += kallio.nimi + ", "
        nimi = input(" " + vaihtoehdot[:-2] + "  ")
        for kallio in kalliot.values(): 
            if nimi.upper() in kallio.nimi.upper() :
                for reitti in kallio.reitit:
                    print(reitti)


def reittiValinnat(valinta): 
    # Etsi
    if valinta == "1":    
        print("\n Millä hakusanalla etsitään? Kategoriat ovat:")
        print("nimi, sektori, pituus, grade, ticks, type, luontipvm. ")
        hakusanat = input("Kirjoita hakusanat (1 tai 2 sanaa), esim. spo 6 tuottaa sport-reitit greideillä 6A-6C+  ")
        # TODO tulee 6.pv luodut, ei hyvä !!!!!!!
        hakusanat = hakusanat.split(" ")

        def search(lookup, reitti):
            for value in reitti.sanakirja.values():
                if lookup.upper() in str(value).upper():    # HUOM! Jotkut arvot int,  osasanat
                    return True

        if len(hakusanat) == 1:
            reitit = [reitti for reitti in kaikki_reitit if search(hakusanat[0], reitti)]   
        if len(hakusanat) == 2:
            reitit = [reitti for reitti in kaikki_reitit if search(hakusanat[0], reitti) and search(hakusanat[1], reitti)]   
        for reitti in reitit:
            print(reitti)

    # Järjestä
    if valinta == "2":    
        print("\n Minkä mukaan järjestetään? Kategoriat ovat:")
        print("nimi, sektori, pituus, grade, ticks, type, luontipvm ")
        hakusanat = input("Anna 1 tai 2 kategoriaa, esim. luontipvm type järjestää ensisijaisesti luontipvm:n mukaan ")
        hakusanat = hakusanat.split(" ")
        if len(hakusanat) == 1:
            for reitti  in jarjesta_reitit_yhden_attribuutin_mukaan(hakusanat[0]):
                print(reitti)
        if len(hakusanat) == 2:
            for reitti  in jarjesta_reitit_kahden_attribuutin_mukaan(hakusanat[0], hakusanat[1]):
                print(reitti)

    # Tikkaa  (tikkaus tehdään myös valinnoissa 5 ja 6)
    if valinta == "3":   
        reitin_nimi = input("\n Mikä reitti tikataan? Voit antaa osan reitin nimestä  ")        
        reitit = [reitti for reitti in kaikki_reitit if reitin_nimi.upper() in reitti.nimi.upper()]   
        for reitti in reitit:
            reitti.tikkaa()  # tekee 4 asiaa
            print(reitti.nimi + " tikattu")

    # Merkkaa projektiksi
    if valinta == "4":  
        reitin_nimi = input("\n Mikä reitti merkataan projektiksi? Voit antaa osan reitin nimestä  ")        
        reitit = [reitti for reitti in kaikki_reitit if reitin_nimi.upper() in reitti.nimi.upper()]   
        for reitti in reitit:
            reitti.projektina = True
            print(reitti.nimi + " on nyt projektisi")

    # Grade-mielipide
    if valinta == "5":
        tiedot = input("\n Anna reitin nimi (tai osanimi) ja greidiavio, esim. possu 6B  ")
        nimi, grade = tiedot.split(" ")
        reitit = [reitti for reitti in kaikki_reitit if nimi.upper() in reitti.nimi.upper()]
        for reitti in reitit:
            reitti.tikkaa()
            reitti.grade_opinion = grade

    # Arvostele reitti
    if valinta == "6":
        tiedot = input("\n Anna reitin nimi (tai osanimi) ja arvosana(1-5), esim. ruo 5  ")
        nimi, arvosana = tiedot.split(" ")
        reitit = [reitti for reitti in kaikki_reitit if nimi.upper() in reitti.nimi.upper()]
        for reitti in reitit:
            reitti.tikkaa()
            reitti.rating = arvosana

    # Näytä reitin henk.koht. tiedot
    if valinta == "7":
        reitin_nimi = input("\n Minkä reitin omat tietosi haluat? Voit antaa osan reitin nimestä  ")        
        reitit = [reitti for reitti in kaikki_reitit if reitin_nimi.upper() in reitti.nimi.upper()]   
        for reitti in reitit:
            print(reitti.nayta_henk_koht_tiedot())


if __name__ == "__main__":

    kalliot = {}    
    openfile()
    kaikki_reitit = muodosta_kaikki_reitit()

    k = Kayttoliittyma()

    while True:
        kallio_vai_reitti = k.valinta1()
        if kallio_vai_reitti == "1":        
            kallioValinnat(k.kallioValinnat())
        elif kallio_vai_reitti == "2":        
            reittiValinnat(k.reittiValinnat())
            pass

    