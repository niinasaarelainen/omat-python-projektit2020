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
                kallion_nimi, ilmansuunta = pari[1].split("#")                      
                kalliot[kallion_nimi] = Kiipeilykallio(kallion_nimi, ilmansuunta)   
                kallio_data = pari
            else:
                reittilista.append(pari)
        if reittilista != [] and kallion_nimi != '':   
            reittilista.append(kallio_data)  
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

def reittien_maaran_mukaan(kalliot:list):     # turha ?!?!?!?
    return sorted(kalliot.values(), key=lambda kallio: kallio.reitteja())   

######  E T S I  ###########
def etsi_reitit_yhden_attribuutin_mukaan(mika_attribuutti, mita_etsitaan):
    reitit = [reitti for reitti in kaikki_reitit if reitti.sanakirja[mika_attribuutti] == mita_etsitaan]        
    return reitit

def etsi_reitit_kahden_attribuutin_mukaan(mika_attribuutti1, mita_etsitaan1, mika_attribuutti2, mita_etsitaan2):
    reitit = [reitti for reitti in kaikki_reitit if reitti.sanakirja[mika_attribuutti1] == mita_etsitaan1 and reitti.sanakirja[mika_attribuutti2] == mita_etsitaan2]        
    return reitit

######  E T S I  --> J Ä R J E S T Ä ###########
def etsi_sitten_jarjesta_reitit(mika_attribuutti1, mita_etsitaan1, mika_attribuutti2):
    reitit = [reitti for reitti in kaikki_reitit if reitti.sanakirja[mika_attribuutti1] == mita_etsitaan1]        
    def yhden_mukaan(reitti):                           # TODO tässä voitaisiin kutsua olemassaol. funktiota
        return reitti.sanakirja[mika_attribuutti2]
    return sorted(reitit, key=yhden_mukaan)  


def kallioValinnat(valinta):
    if valinta == "1":    
        ilmansuunta = input("\n Mitä ilmansuuntaa haet?  ") 
        for kallio in kalliot.values(): 
            if ilmansuunta.upper() in kallio.ilmansuunta.upper() :
                print(kallio.nimi)
    if valinta == "2":           
        vaihtoehdot = ""
        print("\n Minkä kallion reitit printataan? Vaihtoehdot ovat:")
        for kallio in kalliot.values(): 
            vaihtoehdot += kallio.nimi + ", "
        nimi = input(" " + vaihtoehdot[:-2] + "  ")
        for kallio in kalliot.values(): 
            if nimi.upper() in kallio.nimi.upper() :
                for reitti in kallio.reitit:
                    print(reitti)


def reittiValinnat(valinta):  # TODO
    # Etsi
    if valinta == "1":    
        print("\n Millä hakusanalla etsitään? Kategoriat ovat:")
        print("nimi, sektori, pituus, grade, ticks, type, luontipvm. ")
        hakusanat = input("Kirjoita hakusanat (1 tai 2 sanaa), esim. spo 6 tuottaa sport-reitit greideillä 6A-6C+  ")
        hakusanat = hakusanat.split(" ")

        def search(lookup, reitti):
            for value in reitti.sanakirja.values():
                if lookup in str(value):
                    return True

        if len(hakusanat) == 1:
            reitit = [reitti for reitti in kaikki_reitit if search(hakusanat[0], reitti)]   
        if len(hakusanat) == 2:
            reitit = [reitti for reitti in kaikki_reitit if search(hakusanat[0], reitti) and search(hakusanat[1], reitti)]   
        for reitti in reitit:
            print(reitti)
    # Järjestä


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

    