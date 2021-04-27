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
       

def etsi_reitti_hakusanalla(hakusana):
    vastaukset = []
    for kallio in kalliot:
        for reitti in kallio.reitit:
            if hakusana in reitti.nimi:
                vastaukset.append(reitti)
    return vastaukset


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

    kalliot = {}

    openfile()
    print(kalliot)
    print(kalliot["Olhava"].reitit)   # 4 kpl
    print(kalliot["Nalkkila"].reitit)   # 3 kpl
    print("oöhavan ekan reitin sanakirja", kalliot["Olhava"].reitit[0].sanakirja)


    """
    vastaukset = etsi_reitti_hakusanalla("ei")
    monesko = 1
    for reitti in vastaukset:
        print(f"{monesko}. {reitti.nimi}")
        monesko += 1

    print("vaikein_reitti:", kalliot[-1].vaikein_reitti())





     # WANHAT:

    k2 = Kiipeilykallio("Nummi")
    k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))
    k2.lisaa_reitti(Kiipeilyreitti("PidempiSyncro", 15, "8C+"))

        
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