from functools import reduce    # "flatten":ia varten
import datetime  
from luokat import *


def openfile():
    f = open("data.txt", "r")
    data = [rivi.strip().split(",") for rivi in f if rivi.strip() != ''] 
    reittilista = []
    kallion_nimi = ""
    for rivi in data:         
        for item in rivi:   # kallio:olhava   <-- item
            pari = item.split(":")    
            if pari[0] == "kallio":           
                kalliot[pari[1]] = Kiipeilykallio(pari[1])   
                kallion_nimi = pari[1]
            else:
                reittilista.append(pari)
        if reittilista != [] and kallion_nimi != '':   
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
    vastaukset = []
    for kallio in kalliot.values():      # HUOM!   ei pelkkä kalliot !!!!!!!!!!!!
        for reitti in kallio.reitit:
            if hakusana in reitti.sanakirja["nimi"]:
                vastaukset.append(reitti)
    return vastaukset


######  J Ä R J E S T Ä  ###########
def jarjesta_reitit_yhden_attribuutin_mukaan(minka_mukaan):
    def yhden_mukaan(reitti):
        return reitti.sanakirja[minka_mukaan]
    return sorted(kaikki_reitit, key=yhden_mukaan)  

def jarjesta_reitit_kahden_attribuutin_mukaan(minka_mukaan1, minka_mukaan2):
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
    def yhden_mukaan(reitti):
        return reitti.sanakirja[mika_attribuutti2]
    return sorted(reitit, key=yhden_mukaan)  



if __name__ == "__main__":

    kalliot = {}    
    openfile()
    kaikki_reitit = muodosta_kaikki_reitit()
    print("     kaikki_reitit", kaikki_reitit)
    
    print("oöhavan ekan reitin sanakirja", kalliot["Olhava"].reitit[0].sanakirja)    
    vastaukset = etsi_reitti_hakusanalla("ei")
    monesko = 1
    for reitti in vastaukset:
        print(reitti.sanakirja["nimi"])
        #print(f"{monesko}. {reitti.sanakirja["nimi"]}")
        monesko += 1

    # !! metodi luokassa Kiipeilykallio:
    print("\njarjesta_reitit_yhden_attribuutin_mukaan  NIMI  ")
    for reitti in kalliot["Olhava"].jarjesta_reitit_yhden_attribuutin_mukaan("nimi"):
        print(reitti)

    print("\njarjesta_reitit_yhden_attribuutin_mukaan   PIT :")
    for reitti in kalliot["Olhava"].jarjesta_reitit_yhden_attribuutin_mukaan("pituus"):
        print(reitti)

    print("\njarjesta_reitit_yhden_attribuutin_mukaan   grade :")
    for reitti in kalliot["Olhava"].jarjesta_reitit_yhden_attribuutin_mukaan("grade"):
        print(reitti)

    print("\njarjesta_reitit_kahden_attribuutin_mukaan    ticks , nimi:")
    for reitti in kalliot["Olhava"].jarjesta_reitit_kahden_attribuutin_mukaan("ticks", "nimi"):
        print(reitti)        

    print("\nreittien_maaran_mukaan")
    for kallio in reittien_maaran_mukaan(kalliot):
        print(kallio)

    print("\njarjesta_  KAIKKI   reitit_yhden_attribuutin_mukaan  ticks:")
    for reitti in jarjesta_reitit_yhden_attribuutin_mukaan("ticks"):
        print(reitti)

    print("\njarjesta_  KAIKKI   reitit_kahden_attribuutin_mukaan    grade, pit:")
    for reitti in jarjesta_reitit_kahden_attribuutin_mukaan("grade", "pituus"):
        print(reitti)

    print("\njarjesta_  KAIKKI   reitit_kahden_attribuutin_mukaan    tick, grade:")
    for reitti in jarjesta_reitit_kahden_attribuutin_mukaan("tick", "grade"):
        print(reitti)

    print("\netsi_ reitit_yhden_attribuutin_mukaan    grade = 6A+")
    for kallio, reitti in kalliot["Olhava"].etsi_reitit_yhden_attribuutin_mukaan("grade", "6A+"):
        print(f"{kallio}: {reitti}")

    print("\netsi_ reitit_yhden_attribuutin_mukaan   KAIKKI  grade = 6A+")
    for reitti in etsi_reitit_yhden_attribuutin_mukaan("grade", "6A+"):
        print(f"{reitti}")

    print("\netsi_ reitit_kahden_attribuutin_mukaan   KAIKKI  grade = 6A+, ei ole kiivetty")
    for reitti in etsi_reitit_kahden_attribuutin_mukaan("grade", "6A+", "tick", False):
        print(f"{reitti}")


    print("\netsi_sitten_jarjesta_reitit   kiipeämättömät, greidi")
    for reitti in etsi_sitten_jarjesta_reitit("tick", False, "grade"):
        print(reitti)
